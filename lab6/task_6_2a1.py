# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip_address = input('Введите ip адрес:')
ip_address_list = ip_address.split('.')

i = 0
valid_pass = True
range_pass = True

for octet in ip_address_list:
    i += 1


for octet in ip_address_list:
    try:
        int(octet)
    except ValueError:
        valid_pass = False   
        
if valid_pass == True:        
    for octet in ip_address_list:
        if 0 < int(octet) <= 255:
            True
        else:
            range_pass = False



if i != 4 or valid_pass == False or range_pass == False:
    print('Неправильный IP-адрес')
else:
    if int(ip_address_list[0]) <= 223: 
        print('Unicast')
    elif 224 <= int(ip_address_list[0]) <= 239:
        print('Multicast')
    elif ip_address == '255.255.255.255':
        print('Local broadcast')
    elif ip_address == '0.0.0.0':
        print('Unassigned')
    else:
        print('Unused')
