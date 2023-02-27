# -*- coding: utf-8 -*-

'''
Задание 25.1c

Изменить класс Topology из задания 25.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

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
                         
               
if __name__ == '__main__':        
    top = Topology(topology_example)
    print('-'*50)
    top.delete_node('SW1')
    pprint(top.topology)


