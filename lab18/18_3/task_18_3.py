# -*- coding: utf-8 -*-
'''
Задание 18.3

Для заданий 18 раздела нет тестов!

В прошлых заданиях информация добавлялась в пустую БД.
В этом задании, разбирается ситуация, когда в БД уже есть информация.

Скопируйте скрипт add_data.py из задания 18.1 и попробуйте выполнить его повторно, на существующей БД.
Должен быть такой вывод:
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
... (вывод сокращен)

При создании схемы БД, было явно указано, что поле MAC-адрес, должно быть уникальным.
Поэтому, при добавлении записи с таким же MAC-адресом, возникает исключение (ошибка).
В задании 18.1 исключение обрабатывается и выводится сообщение на стандартный поток вывода.

В этом задании считается, что информация периодически считывается с коммутаторов и записывается в файлы.
После этого, информацию из файлов надо перенести в базу данных.
При этом, в новых данных могут быть изменения: MAC пропал, MAC перешел на другой порт/vlan, появился новый MAC и тп.

В этом задании в таблице dhcp надо создать новое поле active, которое будет указывать является ли запись актуальной.
Новая схема БД находится в файле dhcp_snooping_schema.sql

Поле active должно принимать такие значения:
* 0 - означает False. Используется для того, чтобы отметить запись как неактивную
* 1 - True. Используется чтобы указать, что запись активна

Каждый раз, когда информация из файлов с выводом DHCP snooping добавляется заново,
надо пометить все существующие записи (для данного коммутатора), как неактивные (active = 0).
Затем можно обновлять информацию и пометить новые записи, как активные (active = 1).

Таким образом, в БД останутся и старые записи, для MAC-адресов, которые сейчас не активны,
и появится обновленная информация для активных адресов.

Например, в таблице dhcp такие записи:
mac                ip          vlan        interface         switch      active
-----------------  ----------  ----------  ----------------  ----------  ----------
00:09:BB:3D:D6:58  10.1.10.2   10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.5.2    5           FastEthernet0/10  sw1         1
00:05:B3:7E:9B:60  10.1.5.4    5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6   10          FastEthernet0/3   sw1         1
00:09:BC:3F:A6:50  192.168.10  1           FastEthernet0/7   sw1         1


И надо добавить такую информацию из файла:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69   10.1.15.2        63951       dhcp-snooping   15    FastEthernet0/15
00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
00:07:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/5


После добавления данных таблица должна выглядеть так:
mac                ip               vlan        interface         switch      active
-----------------  ---------------  ----------  ---------------   ----------  ----------
00:09:BC:3F:A6:50  192.168.100.100  1           FastEthernet0/7   sw1         0
00:09:BB:3D:D6:58  10.1.10.2        10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.15.2        15          FastEthernet0/15  sw1         1
00:05:B3:7E:9B:60  10.1.5.4         5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6        10          FastEthernet0/5   sw1         1

Новая информация должна перезаписывать предыдущую:
* MAC 00:04:A3:3E:5B:69 перешел на другой порт и попал в другой интерфейс и получил другой адрес
* MAC 00:07:BC:3F:A6:50 перешел на другой порт

Если какого-то MAC-адреса нет в новом файле, его надо оставить в бд со значением active = 0:
* MAC-адреса 00:09:BC:3F:A6:50 нет в новой информации (выключили комп)


Измените скрипт add_data.py таким образом, чтобы выполнялись новые условия и заполнялось поле active.

Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

> Для проверки корректности запроса SQL, можно выполнить его в командной строке, с помощью утилиты sqlite3.

Для проверки задания и работы нового поля, сначала добавьте в бд информацию из файлов sw*_dhcp_snooping.txt,
а потом добавьте информацию из файлов new_data/sw*_dhcp_snooping.txt

Данные должны выглядеть так (порядок строк может быть любым)
-----------------  ---------------  --  ----------------  ---  -
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  0
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  0
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1
00:04:A3:3E:5B:69  10.1.15.2        15  FastEthernet0/15  sw1  1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/5   sw1  1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3  1
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1
00:A9:BC:3F:A6:50  10.1.10.65       20  FastEthernet0/2   sw2  1
00:A9:33:44:A6:50  10.1.10.77       10  FastEthernet0/4   sw2  1
-----------------  ---------------  --  ----------------  ---  -


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
    

def get_old_info_from_db(conn):
    with conn:
        result =  [row[0] for row in conn.execute('SELECT mac from dhcp')]
    return result

def add_info_dhcp_db(conn, snoop_list):
    query_insert = f'INSERT into dhcp values (?,?,?,?,?,1)'
    query_update_active = f'UPDATE dhcp set active = 0 where mac = ?'
    print('Добавляю данные в таблицу dhcp...')
    for line in snoop_list:
        mac, ip, vlan, interface, switch = line
        try:
            with conn:
                conn.execute(query_insert, line)
        except sqlite3.IntegrityError as error:
            print(f'При добавлении данных {line} возникла ошибка', error)
            print('Делаю UPDATE данных')
            print(line)
            try:
                with conn:
                    query_update = f'UPDATE dhcp set ip = "{ip}", vlan = "{vlan}", interface = "{interface}", switch = "{switch}", active = 1 where mac = "{mac}"'
                    #query_update = f'UPDATE dhcp set ip = "{ip}" where mac = "{mac}"'
                    conn.execute(query_update)
            except Exception as error:
                print(error)
    for old_data in get_old_info_from_db(conn):
        old_data_list = []
        if all([old_data not in line[0] for line in snoop_list]):
            with conn:
                old_data_list.append(old_data)
                conn.execute(query_update_active, old_data_list)

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
    conn_session.close()
