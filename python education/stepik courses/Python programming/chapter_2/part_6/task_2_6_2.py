# -*- coding: utf8 -*-

# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

#refactored

n = int(input())

a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
    
print(*a[:n])

#first

# n = int(input())

# s = []
# c = 1
# while len(s) < n:
#     s += [c] * c
#     c += 1

# for i in range(n):
#     print(s[i], end=' ')
