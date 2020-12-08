# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

vlan = input('Введите VLAN:')

with open('CAM_table.txt', 'r') as cam_table:
    cam_table_list = []
    for line in cam_table:
        if 'Gi' in line:
            cam_table_list.append(line.replace('DYNAMIC     ', '').split())
               


for mac_list in cam_table_list:
    mac_list[0] = int(mac_list[0])
        
sorted_mac_list = sorted(cam_table_list)
#for idx in sorted_mac_list:
print(f'{vlan:<8} {idx[1]} {idx[2]:>8}')



