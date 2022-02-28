# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



with open('sh_cdp_n_sw1.txt') as cdp_neighbors:
    cdp_info = cdp_neighbors.read()
    

def parse_cdp_neighbors(command_output):
    command_output_list = command_output.split('\n')
    cdp_neighbors = {}
    for output in command_output_list:
        if 'show cdp neighbors' in output:
            local_device, *rest = output.split('>')
        elif output.startswith('R') or output.startswith('SW'):
#            neighbor_device, local_int, _, _, _, _, neighbot_int = output.split('  ')
            neighbor_device, local_int, *rest, neighbor_int = output.split('       ')
            cdp_neighbors[(local_device.strip(),local_int.strip())] = (neighbor_device.strip(), neighbor_int.strip())
    return cdp_neighbors
            
    
    
a = parse_cdp_neighbors(cdp_info)
print(a)
