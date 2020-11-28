#!/usr/bin/env python3

access_template = ('switchport mode access',
			'switchport access vlan {}',
			'switchport port-security mac-address sticky',
			'switchport port-security maximum {}',
			'shut',
			'no shut')
#type(access_template)
print (type(access_template))
print('\n'.join(access_template).format(3200,2))