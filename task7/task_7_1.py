# -*- coding: utf-8 -*-
#from task4 import task_4_6
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt', 'r') as ospf_table:
    ospf_lines = ospf_table.readlines()

ospf_template = '''
Protocol:              {}
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''

for lines in ospf_lines:
    lines = lines.replace('O        ', 'OSPF ')
    lines = lines.replace(',', '')
    #print(lines)
    route = lines.split()
    via = route.index('via')
    route.pop(via)
    #print(route)
    protocol, prefix, metric, nexthop, lastupdate, intrfc = route
    print(ospf_template.format(protocol, prefix, metric, nexthop, lastupdate, intrfc))








