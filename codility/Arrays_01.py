# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Find value that occurs in odd number of elements.
# НАйти в заданном масииве уникальное число.
# В массиве нечетное число элементов

from random import randint
import timeit, random, itertools, operator, functools

# Тут ошибка именно в непарном элементе...
def solution(A):
    # write your code in Python 3.6
    num_dic = {}

    for i in A:
        if i not in num_dic:
            num_dic[i] = 1
        else:
            num_dic[i] += 1
    # Получили словарь, добавляем словарь в лист

    num_list = []
    for num, value in num_dic.items():
        num_list.append((num, value))
        if value % 2 != 0:
            return num
    # num_list.sort(key=lambda tup: tup[1])
    # print(*num_list)
    # for i in range(len(num_list)):
        # if num_list[i][1] % 2 != 0:
            # digit = num_list[i][0]
            # return digit



#st, fin, num = 1, 100, 201
#lst = []

#for i in range(202):
#    lst.append(randint(st, fin))

# inFile = open('input.txt', 'r', encoding='utf8')
#outFile = open('output.txt', 'w', encoding='utf8')
#lst.sort()

#print(lst, file=outFile)


A = (9, 3, 9, 3, 9, 7, 9)
print(solution(A))
#outFile.close()
