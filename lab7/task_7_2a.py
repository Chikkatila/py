# -*- coding: utf-8 -*-
'''
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Между строками не должно быть дополнительного символа перевода строки.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''



from sys import argv

file_name = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file_name, 'r') as config_sw:
#    print(config_sw.read())
    for line in config_sw:        
        for word in ignore:
            line = line.replace(word, "")
        if line != '!\n' and line != '!         \n' and line != '! \n' and not line.startswith(word):
            print(line.rstrip())

