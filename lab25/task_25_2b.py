# -*- coding: utf-8 -*-

'''
Задание 25.2b

Скопировать класс CiscoTelnet из задания 25.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного режима или список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_25_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

'''


import telnetlib
import time
from textfsm import clitable


r1_params = {'ip': '192.168.1.26',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'}


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'Username:')
        self._write_line(username) 
        self.telnet.read_until(b'Password:')
        self._write_line(password)
        index, m, output = self.telnet.expect([b'>', b'#'])
        if index == 0:
            self._write_line('enable')
            index, m, output = self.telnet.expect([b'Password:', b'#'])
            if index == 0:
                self._write_line(secret)
        self._write_line('terminal length 0')
        self.telnet.read_until(b'#')
    def _write_line(self, string):
        self.telnet.write(string.encode('UTF-8')+b'\n')
    def send_show_command(self, string, template_dir, parse = False):
        self.telnet.write(string.encode('UTF-8')+b'\n')
        result = self.telnet.read_until(b'#')
        if not parse:
            return result.decode('UTF-8')
        else:
            self.cli = clitable.CliTable('index', template_dir)
            self.cli.ParseCmd(result.decode('UTF-8'),{'Command': string})
            return self.cli
    def send_config_commands(self, cmds):
        if type(cmds) == list:
            self._write_line('configure terminal')
            for index in cmds:
                self._write_line(index)
            self._write_line('end')
            time.sleep(5)
            return self.telnet.read_very_eager()
        
        
if __name__ == '__main__':
    r1 = CiscoTelnet(**r1_params)
    #a = r1.send_show_command('show ip int br', 'templates', True)
    a = r1.send_config_commands(['hostname R1', 'int e0/0', 'description WAN_INT'])
    print(a)


