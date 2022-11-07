# -*- coding: utf-8 -*-
'''
Задание 18.2

Для заданий 18 раздела нет тестов!

В этом задании необходимо создать скрипт get_data.py.

Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

Скрипту могут передаваться аргументы и, в зависимости от аргументов, надо выводить разную информацию.
Если скрипт вызван:
* без аргументов, вывести всё содержимое таблицы dhcp
* с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
* с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов

Файл БД можно скопировать из задания 18.1.

Примеры вывода для разного количества и значений аргументов:

$ python get_data.py
В таблице dhcp такие записи:
-----------------  ---------------  --  ----------------  ---
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2
-----------------  ---------------  --  ----------------  ---

$ python get_data.py vlan 10

Информация об устройствах с такими параметрами: vlan 10
-----------------  ----------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2
-----------------  ----------  --  ---------------  ---

$ python get_data.py ip 10.1.10.2

Информация об устройствах с такими параметрами: ip 10.1.10.2
-----------------  ---------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2  10  FastEthernet0/1  sw1
-----------------  ---------  --  ---------------  ---

$ python get_data.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

$ python get_data.py ip vlan 10
Пожалуйста, введите два или ноль аргументов

'''

from sys import argv
import sqlite3
#from pprint import pprint
from tabulate import tabulate

def get_data_from_db(conn, column_name = None, data = None):
    query_all = 'SELECT * from dhcp'
    query_select = f'SELECT * from dhcp where {column_name} GLOB "*{data}*"'
    if not column_name and not data:
        result = [row for row in conn.execute(query_all)]
    else:
        result = [row for row in conn.execute(query_select)]
        #print(result)
    return result if result else None
    


if __name__ == '__main__':
    dbname = 'dhcp_snooping.db'
    conn_session = sqlite3.connect(dbname)
    columns_list = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if len(argv) == 1:
        print('В таблице dhcp такие записи:')
        print(tabulate(get_data_from_db(conn_session)))
    elif len(argv) != 3:
        print('Пожалуйста, введите два или ноль аргументов')
    else:
        dhcp_db_column_name = argv[1]
        dhcp_db_column_data = argv[2]
        if argv[1].lower() not in columns_list:
            print('Данный параметр не поддерживается.')
            print('Допустимые значения параметров: mac, ip, vlan, interface, switch')
        else:
            print(f'Информация об устройствах с такими параметрами: {argv[1]} {argv[2]}')
            print(tabulate(get_data_from_db(conn_session, dhcp_db_column_name, dhcp_db_column_data)))

