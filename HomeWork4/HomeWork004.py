# Практическая работа по семинару 4 

# Задача 1 
'''
Вычислить число c заданной точностью d
Пример:
- при d = 0.001, π = 3.141   
Ввод: 0.01
    Вывод: 3.14

    Ввод: 0.001
    Вывод: 3.141
'''
'''
pi = '3.1415926535897932384626433832795'
n = input("Введите заданную точность : ")
n2 = n.split('.')
kol = len(n2[1])
noliki = range(2,len(n)-1)
for i in range(len(n)):
    if i == 1 and n[i] != '.':
        print("Вы ввели не точные данные! Повторите")
        break
    elif i == 0 and n[i] != '0':
        print("Вы ввели не точные данные! Повторите")
        break
    elif i == len(n) and n[i] != '1':
        print("Вы ввели не точные данные! Повторите")
        break
    elif i == noliki and n[i] != '0':
        print("Вы ввели не точные данные! Повторите")
        break
    else:
        dlina = 1
        while dlina <= kol:
            pi_tochnoe = pi[0:dlina + 2]
            dlina += 1
        print(pi_tochnoe)
        break

'''

# Задача 2
'''
Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''
'''
n = int(input("Введите число : "))

i = 2 
list = []
old = n
while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1

print(list)
'''

# Задача 3 
'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
Ввод: [1, 1, 2, 3, 4, 4, 4]
Вывод: [2, 3]
'''
'''
a = [1, 1, 2, 3, 4, 4, 4]

def NePovtoryaytsya(array: list) -> list:
    list2 = []
    i = 0
    while i < len(array):
        if array.count(array[i]) == 1:
            list2.append(array[i])
        i += 1
    return list2

    
print(NePovtoryaytsya(a))
'''

# Задача 4
'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
'''

import random
k = int(input("Enter k: "))
mnogochlen = []
i = 0
j = k
while i < k :
    
    mnozh = (f'({random.randint(0,11)} * (x ** {j})) +')
    mnogochlen.append(mnozh)
    j -= 1
    i += 1

mnogochlen.append(random.randint(1,10))
res = " ".join(map(str,mnogochlen))
print(res)
file004 = 'HW004.txt'
with open(file004, 'w') as fil:
    fil.writelines(str(res))
    
