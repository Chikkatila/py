#!/usr/bin/env python3

import sys

vlan = sys.argv[1]
max_mac = sys.argv[2]

print(sys.argv)

access_template = ('switchport mode access',
			'switchport access vlan {}',
			'switchport port-security mac-address sticky',
			'switchport port-security maximum {}',
			'shut',
			'no shut')
#type(access_template)
print (type(access_template))
print('\n'.join(access_template).format(vlan,max_mac))