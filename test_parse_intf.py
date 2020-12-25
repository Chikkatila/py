intf_key = ['Ethernet', 'GigabitEthernet']


with open('sh ip int.txt') as intf:
    for line in intf:
        for idx in intf_key:
            if idx in line:
                print(line)
