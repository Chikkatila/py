# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''

import sys
import textfsm

def parse_output_to_dict(template, command_output):
    with open(template) as f:
        parse = textfsm.TextFSM(f)
    headers_list = parse.header
    result_list = parse.ParseText(open(command_output).read())
    final_list = []
    for index in result_list:
        final_list.append({k:v for k,v in zip(headers_list, index)})
    return final_list


print(parse_output_to_dict(sys.argv[1], sys.argv[2]))
