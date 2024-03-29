# -*- coding: utf-8 -*-

'''
Задание 25.2c

Скопировать класс CiscoTelnet из задания 25.2b и изменить метод send_config_commands добавив проверку команд на ошибки.

У метода send_config_commands должен быть дополнительный параметр strict:
* strict=True значит, что при обнаружении ошибки, необходимо сгенерировать исключение ValueError
* strict=False значит, что при обнаружении ошибки, надо только вывести на стандартный поток вывода сообщене об ошибке

Метод дожен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).
Текст исключения и ошибки в примере ниже.

Пример создания экземпляра класса:
In [1]: from task_25_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Использование метода send_config_commands:

In [7]: print(r1.send_config_commands(commands, strict=False))
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
При выполнении команды "i" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "i"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.

'''

import re
import telnetlib
import time
from textfsm import clitable


r1_params = {'ip': '192.168.1.26',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'}


class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.ip = ip
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
        self._write_line(string)
        result = self.telnet.read_until(b'#')
        if not parse:
            return result.decode('UTF-8')
        else:
            self.cli = clitable.CliTable('index', template_dir)
            self.cli.ParseCmd(result.decode('UTF-8'),{'Command': string})
            return self.cli
    def send_config_commands(self, cmds, strict=False):
        def cut_error(output):
            match = re.search(r'(.*)\.\r\n', output.decode('UTF-8'))
            return match.group()
        if type(cmds) == list:
            self._write_line('configure terminal')
            result_output = self.telnet.read_until(b'#')
            for cmd in cmds:
                self._write_line(cmd)
                index, m, output = self.telnet.expect([b'>', b'#', b'%'])
                result_output = result_output+output
                error = self.telnet.read_until(b"#")
                result_output = result_output+error
                if index == 2:
                    error_msg = f'При выполнении команды {cmd} на устройстве {self.ip} возникла ошибка -> {cut_error(error)}'
                    if strict:
                        raise ValueError(error_msg)
                    else:
                        print(error_msg)
            self._write_line('end')
            output = self.telnet.read_until(b"#")
            result_output = result_output+output
            return result_output.decode('UTF-8')


        
        
if __name__ == '__main__':
    r1 = CiscoTelnet(**r1_params)
    #a = r1.send_show_command('show ip int br', 'templates', True)
    good_commands_list = ['hostname R1', 'int e0/0', 'description WAN_INT']
    bad_commands_list = ['hstkr', 'intr eth0/0']
    bad_commands_list2 = ['piska']
    a = r1.send_config_commands(bad_commands_list, False)
    print(a)
