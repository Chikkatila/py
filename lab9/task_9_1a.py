# -*- coding: utf-8 -*-
'''
Задание 9.1a

Сделать копию функции из задания 9.1.

Дополнить скрипт:
* ввести дополнительный параметр, который контролирует будет ли настроен port-security
 * имя параметра 'psecurity'
 * по умолчанию значение None
 * для настройки port-security, как значение надо передать список команд port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_mode_template и шаблона port_security_template, если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

port_security_template = [
    'switchport port-security maximum 2',
    'switchport port-security violation restrict',
    'switchport port-security'
]

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
}


intf_cfg = []
def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    for intf_key, vlan_value in intf_vlan_mapping.items():
        #if "Ethernet" in intf_key:
            #intf_key = intf_key.replace('FastEthernet', 'interface FastEthernet')
            #print(intf_key)
        intf_cfg.append('interface '+intf_key)
        for access_template_line in access_template:
            if 'access vlan' in access_template_line:
                #print(f'{access_template_line} {vlan_value}')
                intf_cfg.append(access_template_line+' '+str(vlan_value))
            else:
                #print(access_template_line)
                intf_cfg.append(access_template_line)
            if psecurity != None:
                for psecurity_line in psecurity:
                  intf_cfg.append(psecurity_line)
        
generate_access_config(access_config, access_mode_template, port_security_template)
print(intf_cfg)
generate_access_config(access_config, access_mode_template, port_security_template)
print(intf_cfg)
