# -*- coding: utf-8 -*-


user_dev = input('Введите имя устройства(r1, r2 или sw1): ')
user_par = input('Введите имя параметра(locationm vendor model, ios, ip, vlans, routing): ')

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}


# думаю в следующих заданиях будут такого рода задания, дальше не продолжаю 
try:
    print(london_co[user_dev][user_par])
except KeyError:
    print("Неправильный ввод")

