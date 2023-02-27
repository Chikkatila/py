# -*- coding: utf-8 -*-


import telnetlib


r1_params = {'ip': '192.168.1.26',
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'}
           
            
def telnet(ip, username, password, secret):
    with telnetlib.Telnet('192.168.1.26') as t:
        z = t.read_until(b'Username:')
        t.write(username.encode('utf-8')+b'\n')    
        t.read_until(b'Password:')
        t.write(password.encode('utf-8')+b'\n')
        t.write(b'enable\n')
        if t.read_until(b'Password:'):
            t.write(secret.encode('utf-8')+b'\n')
        t.write(b'terminal length 0\n')
        output = t.read_very_eager().decode('utf-8')
        return output


print(telnet(**r1_params))
