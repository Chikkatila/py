# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''

import draw_network_graph

def create_network_map(filenames):
    cdp_neighbors = {}
    for filename in filenames:
        with open(filename) as f:
            cdp_neighbors_list= f.readlines()
            for index in cdp_neighbors_list:
                if 'show cdp neighbors' in index:
                    local_device, *rest = index.split('>')
                elif index.startswith('R') or index.startswith('SW'):
                    neighbor_device, local_int, local_int_number, *rest, neighbor_int, neighbor_int_number = index.split()
                    if cdp_neighbors.get((neighbor_device, neighbor_int+neighbor_int_number)) == None:
                        cdp_neighbors[(local_device,local_int+local_int_number)] = (neighbor_device, neighbor_int+neighbor_int_number)
    return cdp_neighbors
            








cdp_files = ['sh_cdp_n_sw1.txt', 'sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt']
cdp_files_test = ['sh_cdp_n_r1.txt']

a = create_network_map(cdp_files)
#rint(a)
draw_network_graph.draw_topology(a)
