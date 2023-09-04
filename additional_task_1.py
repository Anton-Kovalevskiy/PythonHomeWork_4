# задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты случайные от -10 до 10.

# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

from random import randint
k = int(input('Введите натуральное число k -> '))
lib = {}
for i in range (k + 1):
    if i == 0:
        lib[i] = ''
    elif i == 1:
        lib[i] = 'x'
    else:
        lib[i] = 'x^' + str(i)
st = ''
i = k
koef = []
while i >= 0:
    a = randint(-10, 10)
    if a == 0:
        st = st
    if (a > 0) and (i != k):
        st += '+'
    if a == -1:
        st += '-' + lib[i] + ' '
    if a == 1:
        st += '+' + lib[i] + ' '
    else:
        if i == 0:
            st += str(a) + lib[i] + ' '
        else:
            st += str(a) + '*' + lib[i] + ' '
    koef.append(a)
    if i == 0:
        st += '= 0'
    i -= 1

print(st)
print(koef)