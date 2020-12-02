command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
list1 = (command1.split())[-1]
list2 = (command2.split())[-1]
set1 = set(list1.split(','))
set2 = set(list2.split(','))
sets = sorted(set1 & set2)
print(sets)


