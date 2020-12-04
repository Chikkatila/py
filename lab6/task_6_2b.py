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
#ip_address_list = ip_address.split('.')



range_pass = True
ip_address_ok = False

while not ip_address_ok:
    valid_pass = True
    ip_address_list = ip_address.split('.')
    i = 0
    for octet in ip_address_list:
        i += 1


    for octet in ip_address_list:
        try:
            int(octet)
            
        except ValueError:
            valid_pass = False 
            break  
            
    if valid_pass == True:        
        for octet in ip_address_list:
            if 0 < int(octet) <= 255:
                pass
            else:
                range_pass = False
                break



    if i == 4 and valid_pass == True and range_pass == True:
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
        ip_address_ok = True
    else:
        print('Неправильный IP-адрес')
        ip_address = input('Введите ip адрес:')
