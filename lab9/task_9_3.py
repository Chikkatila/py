# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

intfs_list = []
def trunk_template_dict_key(config_filename):
    access_vlan_dict = {}
    trunk_vlan_dict = {}
    with open(config_filename) as file_cfg:
        for line in file_cfg:
            if 'interface' in line:
                intf = line.rstrip()
            elif 'switchport access' in line:
                access_vlan = line.split()[-1]
                access_vlan_dict[intf] = access_vlan
            elif 'switchport trunk' in line:
                trunk_vlan = line.split()[-1].split(',')
                trunk_vlan_dict[intf] = trunk_vlan
        intfs_list.append(access_vlan_dict)
        intfs_list.append(trunk_vlan_dict)
    
            
trunk_template_dict_key("config_sw1.txt")
intfs_tuple = tuple(intfs_list)
#print(access_vlan_dict)
#print('='*80)
#print(trunk_vlan_dict)
print(intfs_list)
print('='*80)
print(intfs_tuple)

