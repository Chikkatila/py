from pprint import pprint

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route_list = ospf_route.split()

prefix = ospf_route_list[1]
ad_metric_key = ospf_route_list[2].strip('[]')
next_hop = ospf_route_list[4].rstrip(',')
last_update = ospf_route_list[5].rstrip(',')
outbound_interface = ospf_route_list[6]

ospf_route_dict = {'Protocol': 'OSPF',
    'Prefix': f'{prefix}',
    'AD/Metric': f'{ad_metric_key}',
    'Next-Hop': f'{next_hop}',
    'Last Update': f'{last_update}',
    'Outbound Interface': f'{outbound_interface}'}


pprint(ospf_route_dict)


