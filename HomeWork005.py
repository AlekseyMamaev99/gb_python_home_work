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
# ---------------------------------------------------------------------------------------------
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
'''
def KonfetyGame(sweets, first_play):
    user_1_count = 0
    user_2_count = 0
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


import random
konfety = 2021
pervyi_hod = random.randint(1,3)
KonfetyGame(50,1)
'''

# ---------------------------------------------------------------------------------------------
# Задача 3
'''
Создайте программу для игры в ""Крестики-нолики"".
'''
'''
ryad_1 = ['1', '2', '3']
ryad_2 = ['4', '5', '6']
ryad_3 = ['7', '8', '9']
pole = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'Привет игроки!\n\
Внимательно взгляните на игровое поле и запомните нумерацию ячеек.\n\
Первым ходит Игрок X!\n\
Игра начинается. Удачи!)\n\
{ryad_1}\n{ryad_2}\n{ryad_3}')


def proverka_win():
    # проверка по горизонтали:
    if ryad_1[0] == ryad_1[1] and ryad_1[0] == ryad_1[2]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_1[0]}')
    elif ryad_2[0] == ryad_2[1] and ryad_2[0] == ryad_2[2]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_2[0]}')
    elif ryad_3[0] == ryad_3[1] and ryad_3[0] == ryad_3[2]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_3[0]}')
    # проверка по вертикали:
    elif ryad_1[0] == ryad_2[0] and ryad_1[0] == ryad_3[0]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_1[0]}')
    elif ryad_1[1] == ryad_2[1] and ryad_1[1] == ryad_3[1]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_1[1]}')
    elif ryad_1[2] == ryad_2[2] and ryad_1[2] == ryad_3[2]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_1[2]}')
    # проверка по диагонали:
    elif ryad_1[0] == ryad_2[1] and ryad_1[0] == ryad_3[2]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_1[0]}')
    elif ryad_1[2] == ryad_2[1] and ryad_1[2] == ryad_3[0]:
        return print(f'Игра окончена!\n Выиграл игрок {ryad_1[2]}')
    # если победитель не выявлен :
    else:
        return -1

def hod_user_x() -> int:
    global x
    x = int(input("Игрок Х! выберите номер поля: "))
    if x in pole:   
        pole.remove(x)
    else:
        print("Такоко поя нет, либо оно уже занято!")
        hod_user_x()
    return x

def hod_user_o():
    global o
    o = int(input("Игрок O! выберите номер поля: "))
    if o in pole:   
        pole.remove(o)
    else:
        print("Такоко поя нет, либо оно уже занято!")
        hod_user_o()
    return o 

def zamena_polya(a: int, b: str):
    if a == 1:
        ryad_1[0] = b
        return ryad_1[0]
    elif a == 2:
        ryad_1[1] = b
        return ryad_1[1]
    elif a == 3:
        ryad_1[2] = b
        return ryad_1[2]
    elif a == 4:
        ryad_2[0] = b
        return ryad_2[0]
    elif a == 5:
        ryad_2[1] = b
        return ryad_2[1]
    elif a == 6:
        ryad_2[2] = b
        return ryad_2[2]
    elif a == 7:
        ryad_3[0] = b
        return ryad_3[0]
    elif a == 8:
        ryad_3[1] = b
        return ryad_3[1]
    elif a == 9:
        ryad_3[2] = b
        return ryad_3[2]


# while proverka_win == "Следующий ход":
while proverka_win() == -1 :
    if len(pole) == 1:
        print("Игра окончена! Ничья!")
        break
    else:
        hod_user_x()
        zamena_polya(x,'x')
        proverka_win()
        print(f' {ryad_1} \n {ryad_2} \n {ryad_3}')
        hod_user_o()
        zamena_polya(o,'o')
        proverka_win()
        print(f' {ryad_1} \n {ryad_2} \n {ryad_3}')
        
'''
# ---------------------------------------------------------------------------------------------
# Задача 4 
'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''
'''
stroka = 'qqqwwwweeerrrrrrrrtyy'
print('Начальная строка: ', stroka)

def szhatie(s: str) -> str:
    list_1 = []
    list_2 = []
    res1 = ''
    for i in s:
        x = str(s.count(i))
        list_1.append(x+i)
    for j in list_1:
        if list_2.count(j) == 0:
            list_2.append(j)
    for k in  list_2:
        res1 += k
    return res1


def vosstanovlenie(s: str) -> str:
    res2 = ''
    list_1 = []
    i = 0
    while i in range(0,len(s)):
        x = int(s[i])
        list_1.append(x * s[i+1])
        i += 2
    for k in list_1:
        res2 += k
    return res2
        
print("Строка после сжатия: ",szhatie(stroka))
print("Строка после восстановления: ",vosstanovlenie(szhatie(stroka)))
'''