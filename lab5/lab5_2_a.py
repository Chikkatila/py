# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_network = input('Введите сеть, которую нужно посчитать: ')
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
