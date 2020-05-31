# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1_get_vlan = command1[command1.find('1')::]
vlans1 = command1_get_vlan.split(',')
command2_get_vlan = command2[command2.find('1')::]
vlans2 = command2_get_vlan.split(',')
set1 = set(vlans1)
set2 = set(vlans2)
set3 = set1 & set2
vlans3 = sorted(list(set3))
print(vlans3)

