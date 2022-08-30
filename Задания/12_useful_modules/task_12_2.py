# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''


import subprocess
import ipaddress

def convert_ranges_to_ip_list(ip_a):
    ip_result = []
    for ip in ip_a:
        try:
            ipaddress.ip_address(ip)
            ip_result.append(ip)
        except ValueError as e:    
            if '-' in ip:
                ip_module = ip.split('.')
                four_octet = ip_module[3].split('-') 
                last_octets = list(range(int(four_octet[0]), int(four_octet[1])+1))
                for last_octet in last_octets:
                    ip = f'{ip_module[0]}.{ip_module[1]}.{ip_module[2]}.{last_octet}'
                    ip_result.append(ip)
    return ip_result
            



if __name__ == '__main__':
    ip_list = ip = ['8.8.8.8', '77.88.8.8', '192.168.200.1-15']
    print(convert_ranges_to_ip_list(ip_list))
