# -*- coding: utf-8 -*-
'''
Задание 4.3

Получить из строки config список VLANов вида:
['1', '3', '10', '20', '30', '100']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
a = config[config.find('1')::]
b = a.split(',')
vlans = config.split()          #Книга
vlans1 = vlans[-1].split(',')   #Книга

print(b)
print(vlans1)

