# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def Task_22 (n, m):
    array_1 = []
    array_2 = []
    for i in range (n):
        array_1.append(int(input(f'Введите {i}-й элемент 1-го множества -> ')))
    for i in range (m):
        array_2.append(int(input(f'Введите {i}-й элемент 2-го множества -> ')))
    print('Получено первое множество: ', array_1)
    print('Получено второе множество: ', array_2)
    array_1 = set(array_1)
    array_2 = set(array_2)
    array_res = list(array_1.intersection(array_2))
    array_res.sort()
    return array_res

n = int(input('Введите количество элементов первого множества -> '))
m = int(input('Введите количество элементов второго множества -> '))

print(Task_22(n, m))




