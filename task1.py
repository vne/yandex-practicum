#!/usr/bin/env python

# Задача 1. Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. 

# Эффективность решения через set: O(N1+N2), требует O(N1+N2) дополнительной памяти на множество и возвращаемый список
# Здесь N1 - длина list1, N2 - длина list2
def solution1(list1, list2):
    set2 = set(list2)
    return [ x for x in list1 if x not in set2 ]

# То же, что solution1, но возвращает генератор, то есть, не требует памяти для хранения промежуточного результата
# Вычислительная сложность O(N1+N2), сложность по памяти O(N2)
def solution2(list1, list2):
    set2 = set(list2)
    for x in list1:
        if x not in set2:
            yield x

# Решение в лоб, вычислительная сложность O(N1*N2), сложность по памяти O(N1)
def solution3(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    return result


if __name__ == '__main__':
    L1 = range(0, 20)
    L2 = range(0, 20, 3)
    print('list 1', list(L1))
    print('list 2', list(L2))
    print('solution 1', solution1(L1, L2))
    print('solution 2', list(solution2(L1, L2)))
    print('solution 3', solution3(L1, L2))
