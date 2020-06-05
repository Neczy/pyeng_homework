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



   

   