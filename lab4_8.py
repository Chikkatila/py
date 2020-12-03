# -*- coding: utf-8 -*-
'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = '192.168.3.1'
ip = ip.split('.')
print(type(ip[0]))
ip_list = []

for idx in ip:
    b = int(idx)
    ip_list.append(b) 
print('{:<8}   {:<8}   {:<8}   {:<8}'.format(ip_list[0],ip_list[1],ip_list[2],ip_list[3],))
print('{:08b}   {:08b}   {:08b}   {:08b}'.format(ip_list[0],ip_list[1],ip_list[2],ip_list[3],))

#print(type(ip_list)
#print(type(ip_list[0]))





