# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''



route_keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']



with open('ospf.txt') as ospf_route:
    for routes in ospf_route:
        i = 0
        routes_list = routes.split()
        routes_list.remove('via')
        for route_lines in routes_list:
            if i<= 5:
                print(f'{route_keys[i]:<20}          {route_lines.strip("[],"):>20}')
                i = i+1

            
                


