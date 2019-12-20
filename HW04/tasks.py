import random
from datetime import datetime
from collections import Counter

NAMES = ['Александр', 'Сергей', 'Владимир', 'Елена', 'Татьяна', 'Андрей', 'Алексей', 'Ольга', 'Николай', 'Наталья',
         'Анна', 'Дмитрий', 'Иван', 'Ирина', 'Мария', 'Светлана', 'Михаил', 'Екатерина', 'Евгений', 'Виктор']

# 1. Напишите функцию (F): на вход список имен и целое число N;
# на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения:
# количество имен 20, N = 100, рекомендуется использовать функцию random);


def get_random_names(names, n):
    return random.choices(names, k=n)


rng_names = get_random_names(NAMES, 100)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;


def get_most_common_name(names):
    return Counter(names).most_common(1)[0][0]


print('самое частое имя из списка: {}'.format(get_most_common_name(rng_names)))

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.


def get_most_rare_letter(names):
    return Counter([name[0] for name in names]).most_common()[-1][0]


print('самая редка буква: {}'.format(get_most_rare_letter(rng_names)))

# PRO: 4.  В файле с логами найти дату самого позднего лога (по метке времени)


def parse_log(path, sep=' - ', tformat='%Y-%m-%d %H:%M:%S,%f'):
    with open(path, 'r', encoding='utf-8') as f:
        return [{
                    'date': datetime.strptime(line[0], tformat),
                    'app': line[1],
                    'log_lvl': line[2],
                    'msg': line[3].rstrip()
                } for line in map(lambda line: tuple(line.split(sep)), f.readlines())]


log = parse_log('log')
latest_time = max([line['date'].time() for line in log])
print(f'дата самого позднего лога по метке времени: {latest_time}')

'''OUT
самое частое имя из списка: Александр
самая редка буква: Д
дата самого позднего лога по метке времени: 23:31:01.338000
'''
