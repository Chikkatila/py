# -*- coding: utf-8 -*-

'''
Задание 25.2

Создать класс CiscoTelnet, который подключается по Telnet к оборудованию Cisco.

При создании экземпляра класса, должно создаваться подключение Telnet, а также переход в режим enable.
Класс должен использовать модуль telnetlib для подключения по Telnet.

У класса CiscoTelnet, кроме __init__, должно быть, как минимум, два метода:
* _write_line - принимает как аргумент строку и отправляет на оборудование строку преобразованную в байты и добавляет перевод строки в конце.
  Метод _write_line должен использоваться внутри класса.
* send_show_command - принимает как аргумент команду show и возвращает вывод полученный с обрудования

Пример создания экземпляра класса:
In [2]: from task_25_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command('sh ip int br')
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

'''

import telnetlib
import time

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
            self.telnet.write(b'enable\n')
            index, m, output = self.telnet.expect([b'Password:', b'#'])
            if index == 0:
                self.telnet.write(secret.encode('utf-8')+b'\n')
        self.telnet.write(b'terminal length 0\n')
        self.telnet.read_until(b'#')
    def _write_line(self, string):
        self.telnet.write(string.encode('UTF-8')+b'\n')
    def send_show_command(self, string):
        self.telnet.write(string.encode('UTF-8')+b'\n')
        result = self.telnet.read_until(b'#')
        return result.decode('UTF-8')
        
        
if __name__ == '__main__':
    r1 = CiscoTelnet(**r1_params)
    a = r1.send_show_command('show clock')
    print(a)

    
        
