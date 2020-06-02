# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from sys import argv

ip_adr = argv[1] # через КМД
#input('Введите IP: ') запрос у пользователя

ip_adr1 = ip_adr.split('.')

index = ip_adr1[0]

index = int(index)

print(index)
if  (ip_adr == '255.255.255.255'):
   print( 'Ip adr: local broadcast')
elif(ip_adr == '0.0.0.0'):
   print( 'Ip adr: unassigned')
elif (index <= 223 and index >= 1 ):
   print('unicast')
elif(index <= 224 and index >= 240):
   print('multicast')
else:
   print('unused')


      

      