# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Введите IP-сеть: ')
newip = ip.split('.')
mask = newip[3].split('/')
newip4 = mask[0]
newip[3] = newip4
tmask = mask[1]
ip1 = int(newip[0])
ip2 = int(newip[1])
ip3 = int(newip[2])
ip4 = int(newip[3])
binip = '{:08b} {:08b} {:08b} {:08b}'.format(ip1, ip2, ip3, ip4)
ip = '{:8} {:8} {:8} {:8}'.format(ip1, ip2, ip3, ip4)
fmask = (8,8,8,8)






print('Network: ', '\n' , ip, '\n', binip, '\n', 'Mask:','\n', tmask)







#print(newip, tmask, newip4)

