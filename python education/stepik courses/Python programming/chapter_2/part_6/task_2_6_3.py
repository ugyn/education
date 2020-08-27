# Напишите программу, которая считывает список чисел lstlst из первой строки и число xx из второй строки, которая выводит все позиции, на которых встречается число xx в переданном списке lstlst.

# Позиции нумеруются с нуля, если число xx не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).

# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

#refactored

lst, x = [int(x) for x in input().split()], int(input())

position = 0
if x in lst:
    for i in lst:
        if x == i:
            print(position, end=' ')
        position += 1
else:
    print('Отсутствует')


#first

# lst, x = [int(x) for x in input().split()], int(input())

# k = True
# c = 0
# for i in lst:
#     if x == i:
#         print(c, end=' ')
#         k = False
#     c += 1

# if k:
#     print('Отсутствует')