
# -*- coding: utf-8 -*-
'''
Задание 18.1

Для заданий 18 раздела нет тестов!

Необходимо создать два скрипта:

1. create_db.py
2. add_data.py


1. create_db.py - в этот скрипт должна быть вынесена функциональность по созданию БД:
  * должна выполняться проверка наличия файла БД
  * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql, должна быть создана БД
  * имя файла бд - dhcp_snooping.db

В БД должно быть две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - тут хранится информация полученная из вывода sh ip dhcp snooping binding

Пример выполнения скрипта, когда файла dhcp_snooping.db нет:
$ python create_db.py
Создаю базу данных...

После создания файла:
$ python create_db.py
База данных существует


2. add_data.py - с помощью этого скрипта, выполняется добавление данных в БД. Скрипт должен добавлять данные из вывода sh ip dhcp snooping binding и информацию о коммутаторах

Соответственно, в файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Пример выполнения скрипта, когда база данных еще не создана:
$ python add_data.py
База данных не существует. Перед добавлением данных, ее надо создать

Пример выполнения скрипта первый раз, после создания базы данных:
$ python add_data.py
Добавляю данные в таблицу switches...
Добавляю данные в таблицу dhcp...

Пример выполнения скрипта, после того как данные были добавлены в таблицу (порядок добавления данных может быть произвольным, но сообщения должны выводиться аналогично выводу ниже):
$ python add_data.py
Добавляю данные в таблицу switches...
При добавлении данных: ('sw1', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
При добавлении данных: ('sw2', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
При добавлении данных: ('sw3', 'London, 21 New Globe Walk') Возникла ошибка: UNIQUE constraint failed: switches.hostname
Добавляю данные в таблицу dhcp...
При добавлении данных: ('00:09:BB:3D:D6:58', '10.1.10.2', '10', 'FastEthernet0/1', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:04:A3:3E:5B:69', '10.1.5.2', '5', 'FastEthernet0/10', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:05:B3:7E:9B:60', '10.1.5.4', '5', 'FastEthernet0/9', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:07:BC:3F:A6:50', '10.1.10.6', '10', 'FastEthernet0/3', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:E9:BC:3F:A6:50', '100.1.1.6', '3', 'FastEthernet0/20', 'sw3') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:E9:22:11:A6:50', '100.1.1.7', '3', 'FastEthernet0/21', 'sw3') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:A9:BB:3D:D6:58', '10.1.10.20', '10', 'FastEthernet0/7', 'sw2') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:B4:A3:3E:5B:69', '10.1.5.20', '5', 'FastEthernet0/5', 'sw2') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:C5:B3:7E:9B:60', '10.1.5.40', '5', 'FastEthernet0/9', 'sw2') Возникла ошибка: UNIQUE constraint failed: dhcp.mac
При добавлении данных: ('00:A9:BC:3F:A6:50', '10.1.10.60', '20', 'FastEthernet0/2', 'sw2') Возникла ошибка: UNIQUE constraint failed: dhcp.mac


На данном этапе, оба скрипта вызываются без аргументов.

Код в скриптах должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

'''


import sqlite3
import os
import re
import yaml
from yaml.loader import SafeLoader
  
def create_db_scheme(conn, db, f_exist, scheme):
    if not f_exist:
        print('Создаю базу данных...')
        with open(scheme) as f:
            conn.executescript(f.read())
    else:
        print('База данных существует')
        

def get_switches_info(filename):
    with open(filename) as yaml_f:
        return yaml.load(yaml_f, Loader=SafeLoader)


def parse_snooping_output(text):
    return re.findall('(\S+) +(\S+).*dhcp-snooping +(\d+) +(\S+)', text)


def parse_snooping_tables(snooping_list):
    big_snooping_list = []
    for snooping in snooping_list:
        hostname, *_ = snooping.split('_')
        with open (snooping) as f:
            parse_result_list = parse_snooping_output(f.read())
        for snoop_tuple in parse_result_list:
            snoop_list = list(snoop_tuple)
            snoop_list.append(hostname)
            big_snooping_list.append(snoop_list)
    return big_snooping_list
                  

def add_info_switches_db(conn, devices_dict):
    query = 'INSERT into switches values (?,?)'
    for key, value in devices_dict.items():
        for hostname, location in value.items():
            line = (hostname, location)
            try:
                print('Добавляю данные в таблицу switches...')
                with conn:
                    conn.execute(query, line)
            except sqlite3.IntegrityError as error:
                print(f'При добавлении данных {line} возникла ошибка', error)
    

def add_info_dhcp_db(conn, snoop_list):
    query = 'INSERT into dhcp values (?,?,?,?,?)'
    for line in snoop_list:
            try:
                print('Добавляю данные в таблицу dhcp...')
                with conn:
                    conn.execute(query, line)
            except sqlite3.IntegrityError as error:
                print(f'При добавлении данных {line} возникла ошибка', error)


if __name__ == '__main__':
    dbname = 'dhcp_snooping.db'
    scheme_name = 'dhcp_snooping_schema.sql'
    switches_info = 'switches.yml'
    dhcp_files_list=['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    file_exist = os.path.exists(dbname)
    conn_session = sqlite3.connect(dbname)
    create_db_scheme(conn_session, dbname, file_exist, scheme_name)
    switches_dict = get_switches_info(switches_info)
    add_info_switches_db(conn_session, switches_dict)
    snooping_list = parse_snooping_tables(dhcp_files_list)
    add_info_dhcp_db(conn_session, snooping_list)
