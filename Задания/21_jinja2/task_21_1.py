# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''

import sys
import os
import yaml
import jinja2


def generate_config(template, data_dict):
    template_dir, template_file = os.path.split(template)
    env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(template_dir),
        trim_blocks = True,
        lstrip_blocks = True)
    template = env.get_template(template_file)
    with open(data_dict) as f:
        vars_dict = yaml.load(f, Loader=yaml.loader.SafeLoader)
    return template.render(vars_dict)
    
    
if __name__ == '__main__':
    print(generate_config(sys.argv[1], sys.argv[2]))
