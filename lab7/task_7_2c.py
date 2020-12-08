# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


from sys import argv

src_file_name = argv[1]

dst_file_name = argv[2]

ignore = ['duplex', 'alias', 'Current configuration']

with open(src_file_name, 'r') as config_sw, open(dst_file_name, 'w') as dest_config_sw:
#    print(config_sw.read())
    for line in config_sw:        
        for word in ignore:
            line = line.replace(word, "")
        if not line.startswith(word):
#            print(line.rstrip('\n'))
            dest_config_sw.write(line)
            
