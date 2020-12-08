# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


from sys import argv

file_name = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file_name, 'r') as config_sw, open('config_sw1_cleared.txt', 'w') as dest_config_sw:
#    print(config_sw.read())
    for line in config_sw:        
        for word in ignore:
            line = line.replace(word, "")
        if not line.startswith(word):
#            print(line.rstrip('\n'))
            dest_config_sw.write(line)
            
