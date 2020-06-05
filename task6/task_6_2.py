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
<<<<<<< HEAD

user_input_ip =input('Введите IP-адресс в формате 8.8.8.8: ')

oct_user_input_ip = user_input_ip.split('.')

foctet = oct_user_input_ip[0]

foctet = int(foctet)

ip_add_type = ['unicast', 'multicast', 'local broadcast', 'unassigned', 'unused']

if user_input_ip == '255.255.255.255':
   print('Ip-adress', ip_add_type[2])
elif user_input_ip == '0.0.0.0':
   print('Ip-adress', ip_add_type[3])
elif (foctet <= 223 and foctet >= 1):
   print('Ip-adress', ip_add_type[0]) 
elif (foctet <= 239 and foctet >= 224):
   print('Ip-adress', ip_add_type[0]) 
else:
   print('Ip-adress', ip_add_type[4])



   

   
=======
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


      

      
>>>>>>> 3eb1e250815d7154823dee5a78f16d1737da170b
