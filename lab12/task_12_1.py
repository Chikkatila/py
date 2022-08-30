# -*- coding: utf-8 -*-



'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


import subprocess
import ipaddress


def ping_ip_addresses(ip_list):
    ip_ok_list = []
    ip_neok_list = []
    for ip in ip_list:
        print(f'Пингую {ip}')
        ping_result = subprocess.run(f'ping {ip} -c 3', shell=True,  stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
        #print(ping_result.stdout)
        if ping_result.returncode == 0:
            print('Хост доступен')
            ip_ok_list.append(ip)
        else:
            print('Хост НЕдоступен')
            ip_neok_list.append(ip)
    return (ip_ok_list, ip_neok_list)

if __name__ == '__main__':
    ip = ['8.8.8.8', '77.88.8.8', '192.168.200.200']
    result = ping_ip_addresses(ip)
    print(result)


