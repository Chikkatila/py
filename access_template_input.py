#!/usr/bin/env python3

#import sys

intf = input('Введите интерфейс: ')
vlan = input('Введите номер вилана: ')
max_mac = input('Введите количество доверенных mac адресов: ')

#print(sys.argv)

access_template = ('switchport mode access',
			'switchport access vlan {}',
			'switchport port-security mac-address sticky',
			'switchport port-security maximum {}',
			'shut',
			'no shut')
#type(access_template)
#print (type(access_template))
print('Interface {}'.format(intf))
print('\n'.join(access_template).format(vlan,max_mac))