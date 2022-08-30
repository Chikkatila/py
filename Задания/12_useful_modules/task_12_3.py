# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
'''
from tabulate import tabulate


def print_ip_table(good_ip_list, bad_ip_list):
    for a, b in good_ip_list, bad_ip_list:
        if not b:
            print('GOVNO')
    
#    ip_list = []
#    for good in good_ip_list:
#       ip_dict = {}
#        ip_dict['Reachable'] = good
#        ip_list.append(ip_dict)
#    print(ip_list)
   
    
    
if __name__ == '__main__':
    good_ip = ['8.8.8.8', '77.88.8.8']
    bad_ip = ['1.1.1.1', '192.168.200.200', '2.2.2.2']
    table = print_ip_table(good_ip, bad_ip)
    #print(table)
