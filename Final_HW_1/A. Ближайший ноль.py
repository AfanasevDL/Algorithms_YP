"""A. Ближайший ноль"""

"""Формат ввода.
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). 
В следующей строке записаны n целых неотрицательных чисел — номера домов 
и обозначения пустых участков на карте (нули). 
Гарантируется, что в последовательности есть хотя бы один ноль. 
Номера домов (положительные числа) уникальны и не превосходят 109."""

"""Формат вывода.
Для каждого из участков выведите расстояние до ближайшего нуля. 
Числа выводите в одну строку, разделяя их пробелами."""

""" ID 67950720 Компилятор Python 3.7.3 Время 1.345s Память 135.52Mb"""

n = int(input())
house_numbers = input().split()


def def_distances(n, house_numbers):
    distance = n
    for i in house_numbers:
        if i == '0':
            distance = 0
        else:
            distance += 1
        yield distance


dist_forward = def_distances(n, house_numbers)
dist_backward = reversed(tuple(def_distances(n, reversed(house_numbers))))

print(*map(min, zip(dist_forward, dist_backward)))