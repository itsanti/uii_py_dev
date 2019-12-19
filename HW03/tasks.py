import pymorphy2
from collections import Counter

# читаем файл в переменную
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1) методами строк очистить текст от знаков препинания;
for char in ',.-—(«»)!;?:':
    text = text.replace(char, '')

# 2) сформировать list со словами (split);
words = text.split()

# 3) привести все слова к нижнему регистру (map);
words = list(map(str.lower, words))

# PRO: 6) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
# Лемматизация – это процесс преобразования слова в его базовую форму.

morph = pymorphy2.MorphAnalyzer()
words = list(map(lambda word: morph.parse(word)[0].normal_form, words))

# 4) получить из list пункта 3 (6) dict, ключами которого являются слова, а значениями их количество появлений в тексте;
words_count = {
    word: words.count(word) for word in words
}

# 5) вывести 5 наиболее часто встречающихся слов (sort)

print('words count')
for word, count in sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:5]:
    print(f'{word:4} {count:>6}')

'''OUT:
words count
и        36
в        29
он       29
не       19
с        17
'''

# вывести количество разных слов в тексте (set).
print(len(set(words)))   # 319 слов
print(len(words_count))  # 319 слов - ключи в словаре - уникальные слова

# посчитать частоту и вывести топ 5 слов проще с классом Counter из модуля collections
words_count = Counter(words)
print('words count: Counter')
for word, count in words_count.most_common(5):
    print(f'{word:4} {count:>6}')

'''OUT
words count: Counter
и        36
в        29
он       29
не       19
с        17
'''
