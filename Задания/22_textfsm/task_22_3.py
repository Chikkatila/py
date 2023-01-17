# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
import os
from textfsm import clitable

def parse_command_dynamic(command_output, attributes_dict, index_file, templ_path):
    cli = clitable.CliTable(index_file, templ_path)
    cli.ParseCmd(command_output, attributes_dict)
    intf_list = [list(index) for index in cli]
    headers_list = intf_list.pop(0)
    result_list = []
    for index in intf_list:
        result_list.append({k:v for k, v in zip(cli.header, index)})
    return result_list
    
    
    

command_dict = {'Command': 'sh ip int br',
                'Vendor': 'cisco_ios'}
path, filename = os.path.split('templates/index')
finish_result = parse_command_dynamic(open('output/sh_ip_int_br.txt').read(), command_dict, filename, path)
for result_index in finish_result:
    print(result_index)


