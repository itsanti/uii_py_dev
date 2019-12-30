from time import time
from functools import wraps
from utils.tools import bytes2human
import os
import sys
import psutil


# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.
# используем @wraps, чтобы задать __name__ для декорируемой функции
def timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        return f(*args, **kwargs), time() - start
    return wrapper


# 2. Сравнить время создания генератора и списка с элементами:
# натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
@timeit
def create_from_generator(a, b):
    return [x for x in range(a, b + 1)]


@timeit
def create_from_list(a, b):
    result = []
    for i in range(a, b + 1):
        result.append(i)
    return result


N = 1000000
print(f'N = {N}')
result, sec = create_from_generator(1, N)
print(f'{create_from_generator.__name__}: list_len={len(result)}, gen_time={sec:.4f} sec.')
result, sec = create_from_list(1, N)
print(f'{create_from_list.__name__:>21}: list_len={len(result)}, gen_time={sec:.4f} sec.')


# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
def get_memory(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start = proc.memory_info().rss
        return f(*args, **kwargs), bytes2human(proc.memory_info().rss - start)
    return wrapper


create_from_generator = get_memory(create_from_generator)
result, memory = create_from_generator(1, N)
print(f'{create_from_generator.__name__}: list_len={len(result[0])}, memory={memory}')
create_from_list = get_memory(create_from_list)
result, memory = create_from_list(1, N)
print(f'{create_from_list.__name__:>21}: list_len={len(result[0])}, memory={memory}')


@get_memory
def create_from_func_generator(a, b):
    for x in range(a, b + 1):
        yield x


result, memory = create_from_func_generator(1, N)
print(f'{create_from_func_generator.__name__}: memory={memory}, result_memory={bytes2human(sys.getsizeof(result))}')


'''OUT
N = 1000000
create_from_generator: list_len=1000000, gen_time=0.0550 sec.
     create_from_list: list_len=1000000, gen_time=0.0910 sec.
create_from_generator: list_len=1000000, memory=38.5M
     create_from_list: list_len=1000000, memory=38.4M

N = 100000000
create_from_generator: list_len=100000000, gen_time=6.3599 sec.
     create_from_list: list_len=100000000, gen_time=10.3696 sec.
create_from_generator: list_len=100000000, memory=3.8G
     create_from_list: list_len=100000000, memory=3.8G
     
create_from_func_generator: memory=0B, result_memory=120B

Вывод:
1. создание списков с помощью генератора (list comprehension) работает быстрее.
2. создание списка в памяти на 1000000 элементов потребляет 38 мегабайт памяти,
а использование объекта-генератора позволяет сократить количество необходимой памяти до 120 байт (объект генератора)
'''
