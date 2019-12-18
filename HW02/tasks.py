'''
Задача 1

Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

for k in range(1, 6):
    print(k, 0)

'''
Задача 2

Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

fives = 0
for k in range(1, 11):
    if int(input('Введите число ' + str(k) + ': ')) == 5:
        fives += 1
print('fives count:', fives)

'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

s_ = 0
for k in range(1, 101):
    s_ += k
print('сумма ряда чисел от 1 до 100:', s_)

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

p = 1
for k in range(1, 11):
    p *= k
print('произведение ряда чисел от 1 до 10:', p)

'''
Задача 5

Вывести цифры числа на каждой строчке.
'''

integer_number = 2129
size = len(str(integer_number)) - 1

while size >= 0:
    print(integer_number // 10 ** size)
    integer_number %= 10 ** size
    size -= 1

'''
Задача 6

Найти сумму цифр числа.
'''

integer_number = 123321
s_ = 0
while integer_number > 0:
    s_ += integer_number % 10
    integer_number //= 10
print('сумма цифр числа 123321:', s_)

'''
Задача 7

Найти произведение цифр числа.
'''

integer_number = 1234
p = 1
while integer_number > 0:
    p *= integer_number % 10
    integer_number //= 10
print('произведение цифр числа 1234:', p)

'''
Задача 8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

integer_number = 12534
while integer_number > 0:
    if integer_number % 10 == 5:
        print('Yes, five exists in number.')
        break
    integer_number //= 10
else:
    print('No, five not exists in number.')

'''
Задача 9

Найти максимальную цифру в числе
'''

integer_number = 123978
max_ = 0

while integer_number > 0:
    max_ = integer_number % 10 if integer_number % 10 > max_ else max_
    integer_number //= 10
print('max digit in number:', max_)

'''
Задача 10

Найти количество цифр 5 в числе
'''

integer_number = 1255345
fives = 0

while integer_number > 0:
    if integer_number % 10 == 5:
        fives += 1
    integer_number //= 10
print('fives count in 1255345:', fives)
