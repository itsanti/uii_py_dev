'''
  Все функции модуля принимают на вход натуральные числа от 1 до 1000.
'''

from math import sqrt
from collections import Counter


# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


# 1.1) исползуя все делители числа
def is_prime_(n):
    return len(get_divisors(n)) == 2


# 2) выводит список всех делителей числа;
def get_divisors(n):
    result = []
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            if n / i == i:
                result.append(i)
            else:
                result.extend([i, n // i])
        i = i + 1
    result.sort()
    return result


# 3) выводит самый большой простой делитель числа.
def get_max_prime_divisor(n):
    if n == 1:
        return None
    return max(list(filter(is_prime, get_divisors(n))))


# PRO
# 4) функция выводит каноническое разложение числа на простые множители;
def canonical_decomposition(n, format=False):
    result = []
    if not is_prime(n):
        while n > 1:
            p = get_max_prime_divisor(n)
            result.append(p)
            n //= p
    if format and is_prime(n):
        result = 'prime number'
    elif format:
        r = sorted(Counter(result).items())
        result = ''
        for item in r:
            result += f'{item[0]} * ' if item[1] == 1 else f'{item[0]} ^ {item[1]} * '
        result = result[:-3]
    return result


# 5)функция выводит самый большой делитель (не обязательно простой) числа.
# наибольший, отличный от самого числа
def get_max_divisor(n):
    if n == 1:
        return None
    return max(get_divisors(n)[:-1])
