ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route_new = ospf_route.replace('O','OSPF')



ospf_route_list = ospf_route_new.split()
route_keys = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-hop:', 'Last update:', 'Outbound Interface:']
ospf_route_list.remove('via')
### ospf_route_list = ['OSPF', '10.0.24.0/24', '[110/41]', '10.0.13.3,', '3d18h,', 'FastEthernet0/0']

i=0

while i < 5:
    print('{:<20}'.format(route_keys[i])+'    '+'{:>20}'.format(ospf_route_list[i].strip('[], ')))
    i += 1
    



