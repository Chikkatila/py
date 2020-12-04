# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_address = input('Введите ip адрес:')

ip_address_list = ip_address.split('.')


if int(ip_address_list[0]) <= 223:
    print('Unicast')
elif 224 <= int(ip_address_list[0]) <= 239:
    print('Multicast')
elif ip_address == '255.255.255.255':
    print('Local broadcast')
elif ip_address == '0.0.0.0':
    print('Unassigned')
else:
    print('Unused')
