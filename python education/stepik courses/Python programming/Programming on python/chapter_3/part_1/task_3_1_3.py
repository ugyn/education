# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

#best

def modify_list(l):
    l[:] = [i // 2 for i in l if not i % 2]

#other language-like

# def modify_list(l):
#     temp = []
#     while l:
#         x = l.pop()
#         if not x % 2 == 1:
#             temp.append(x)
#     while temp:
#         l.append(temp.pop() // 2)

#first

# def modify_list(l):
#     n = 0
#     l += ' '
#     while l[n] != ' ':
#         if l[n] % 2 == 0:
#             l[n] //= 2
#             n += 1
#         else:
#             l.remove(l[n])
#     l.remove(l[n])
        
