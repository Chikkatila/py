# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

'''
import sys
import textfsm

def parse_command_output(template, command_output):
    with open(template) as f:
        parse = textfsm.TextFSM(f)
    a = parse.ParseText(open(command_output).read())
    a.insert(0, parse.header)
    return a
    
    

print(parse_command_output(sys.argv[1], sys.argv[2]))
