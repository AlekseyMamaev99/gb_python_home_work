'''
Практическая рвбота по семинару №3

# Задача 1 
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной идексах.
Пример:
[2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12


def summa_nechotnyh(list: list) -> int:
    sum = 0 
    for i in range(len(list)):
        if i %2 != 0 :
            sum += list[i]
    return sum

list = [2, 3, 5, 9, 3]
print(summa_nechotnyh(list))
'''
'''
# Задача 2 
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]


def proizvedenie_el_list(list: list) -> list:
    list2 = []
    k = 0
    if len(list) %2 == 0:
        for i in range((len(list)//2)):
            x = list[i] * list[-i-1]
            list2.append(x)
    else:
        while k <= (len(list)//2):
            y = list[k] * list[-k-1]
            list2.append(y)
            k += 1
    return list2

list1 = [2, 3, 5, 6]
list2 = [2, 3, 4, 5, 6]
print(list1,"->",proizvedenie_el_list(list1))
print()
print(list2, "->", proizvedenie_el_list(list2))
'''

'''
# Задача 3
Задайте список из вещественных чисел. Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 10.01] => 0.19



'''
'''
# Задача 4
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10


def v_dvoichnoe(numbers: int) -> int:
    bin_nums = ""
    while numbers > 0:
        bin_nums += str(numbers % 2)
        numbers //= 2
    return bin_nums

n = int(input("Введите число: "))
print(v_dvoichnoe(n))
'''

'''
# Задача 5
Задайте число. 
Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



def fibonacci_list(n: int) -> list:
    fib_list = [-1, 1, 0, 1, 1]
    for i in range(3, n+1):
        fib_list.append(fib_list[-2] + fib_list[-1])
        fib_list.insert(0, fib_list[1] - fib_list[0])
    return fib_list


n = int(input('Введите число большее 2: '))
if n < 2:
    print("Вы ввели число меньше чем 2!!!")
else:
    list = fibonacci_list(n)
    print(list)
'''