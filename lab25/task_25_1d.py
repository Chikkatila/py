# -*- coding: utf-8 -*-

'''
Задание 25.1d

Изменить класс Topology из задания 25.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


'''

import copy
from pprint import pprint


topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}


class Topology:
    def __init__(self, topology_dict):
        self.normalized = False
        if self.normalized:
            self.topology = self._normalize(topology_dict)
        else:
            self.topology = topology_dict
            
    def _normalize(self, topology_dict):
        result_dict = {}
        for key, value in topology_dict.items():
            if not result_dict.get(value):
                result_dict[key] = value
        self.topology = result_dict
        self.normalized = True
        
    def delete_link(self, *bad_link):
        if bad_link:
            if self.topology.get(bad_link[0]) and self.topology.get(bad_link[1]):               
                del self.topology[bad_link[0]]
                del self.topology[bad_link[1]]
            elif self.topology.get(bad_link[0]):
                del self.topology[bad_link[0]]
            elif self.topology.get(bad_link[1]):
                del self.topology[bad_link[1]]
            else:
                print('Такого соединения нет')
    
    def delete_node(self, hostname):
        temp_dict = copy.deepcopy(self.topology)
        for key, value in temp_dict.items():
            if hostname in key[0]:
                del self.topology[key]
            if hostname in value[0]:
                del self.topology[key]
                
    def add_link(self, k, v):
        temp_dict = copy.deepcopy(self.topology)
        have_link = False
        for key, value in temp_dict.items():
            print(k, key)
            print(v, value)
            if k == key and v == value:
                print("Такое соединение существует") 
                have_link = True
            elif k == key or v == value or k == value or v == key:
                print("Cоединение с одним из портов существует")
                have_link = True
            break
        if not have_link:
            self.topology[k] = v
            print("Cоединение добавлено")
                                
               
if __name__ == '__main__':        
    top = Topology(topology_example)
    print('-'*50)
    top.add_link(('SW1', 'Eth0/1'), ('R1', 'Eth0/0'))
    pprint(top.topology)

