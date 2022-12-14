# Задача 1
'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
'''
strin = 'Я люблю абвЖвау иабв Питон'
my_li = strin.split()
my_li = list(filter(lambda el: not "абв" in el, my_li))
print(my_li)
my_string = " ".join(my_li)
print(my_string)
'''

# Задача 2
'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''
import random

konfety = 2021
pervyi_hod = random.randint(1,3)

def KonfetyGame(konfety, first_play):
    user_1_count = 0
    user_2_count = 0
    sweets = konfety
    while sweets > 0:
        if sweets < 28:
            max_hod = sweets + 1
        else:
            max_hod = 29
        if first_play == 1:
            hod_1 = int(input('Игрок 1. Введите кол-во конфет которое хотите взять (максимум 28): '))
            if hod_1 in range(1,max_hod):
                user_1_count += hod_1
                sweets -= hod_1
                print("Осталось конфет: ", sweets)
            else:
                print('Вы взяли слишком много конфет! ')
        
            hod_2 = int(input('Игрок 2. Введите кол-во конфет которое хотите взять (максимум 28): '))
            if hod_2 in range(1,max_hod):
                user_2_count += hod_2
                sweets -= hod_2
                print("Осталось конфет: ", sweets)
            else:
                print('Вы взяли слишком много конфет! ')
        else:
            hod_2 = int(input('Игрок 2. Введите кол-во конфет которое хотите взять (максимум 28): '))
            if hod_2 in range(1,max_hod):
                user_2_count += hod_2
                sweets -= hod_2
                print("Осталось конфет: ", sweets)
            else:
                print('Вы взяли слишком много конфет! ')
            
            hod_1 = int(input('Игрок 1. Введите кол-во конфет которое хотите взять (максимум 28): '))
            if hod_1 in range(1,max_hod):
                user_1_count += hod_1
                sweets -= hod_1
                print("Осталось конфет: ", sweets)
            else:
                print('Вы взяли слишком много конфет! ')

KonfetyGame(50,1)


        
