# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            elif 'switchport mode access' in line:
                access_vlan_dict[intf] = '1'
            elif 'switchport trunk allowed' in line:
                trunk_vlan = line.split()[-1].split(',')
                trunk_vlan_dict[intf] = trunk_vlan
        intfs_list.append(access_vlan_dict)
        intfs_list.append(trunk_vlan_dict)
    
            
trunk_template_dict_key("config_sw2.txt")
intfs_tuple = tuple(intfs_list)
#print(access_vlan_dict)
#print('='*80)
#print(trunk_vlan_dict)
#print(intfs_list)
#print('='*80)
print(intfs_tuple)
