# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

arg_network = argv[1]
arg_prefix = argv[2]
ip_network = arg_network+'/'+arg_prefix
ip_network_list = ip_network.split('/')
network = ip_network_list[0]
#Разбиваем значение ip адреса на список
network = network.split('.')
network.insert(3, '0')
network.pop()

#Задаем переменную для префикса
prefix = ip_network_list[1]
#Создаем словарь с масками
mask_dict = {'24': '255.255.255.0',
    '25': '255.255.255.128',
    '26': '255.255.255.192',
    '27': '255.255.255.224'}
#Разбиваем значение ip масок на список
mask_list = mask_dict[prefix].split('.')


print('Network:')
print('{:<8}   {:<8}   {:<8}   {:<8}'.format((network[0]),(network[1]),(network[2]),(network[3])))
print('{:08b}   {:08b}   {:08b}   {:08b}'.format(int(network[0]),int(network[1]),int(network[2]),int(network[3])))
print('========='*5)
print('Mask:')
print('/'+prefix)
print('{:<8}   {:<8}   {:<8}   {:<8}'.format((mask_list[0]),(mask_list[1]),(mask_list[2]),(mask_list[3])))
print('{:08b}   {:08b}   {:08b}   {:08b}'.format(int(mask_list[0]),int(mask_list[1]),int(mask_list[2]),int(mask_list[3])))

