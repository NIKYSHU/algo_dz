from random import randint
from copy import copy

some_list = [randint(0, 9) for i in range(10)]
some_list_orig = copy(some_list)


min_value = min(some_list)
max_value = max(some_list)

modifications = []

for idx, number in enumerate(some_list):
    if number == min_value:
        modifications.append((idx, max_value))
    elif number == max_value:
        modifications.append((idx, min_value))


for idx, val in modifications:
    some_list[idx] = val

print('Оригинальный список:\n', some_list_orig)
print('Измененный список:\n', some_list)
print(f'Меняли местами {max_value} и {min_value}')