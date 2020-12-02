ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route_new = ospf_route.replace('O','OSPF')
ospf_route_list = ospf_route_new.split()
route_keys = ['Protocol:', 'Prefix:', 'AD/Metric:', 'Next-hop:', 'Last update:', 'Outbound Interface:']
route_dict = dict.fromkeys(route_keys)
print(route_dict)
print('======='*10)

i = 0

for key in route_keys:
    a = {str(key):ospf_route_list[i]}
    route_dict.update(a)
    i += 1
#    for item in ospf_route_list:

print(route_dict)     
    



