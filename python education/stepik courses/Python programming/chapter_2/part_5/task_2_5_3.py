# Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

# Используйте метод split строки. 

#first

numbers = input().split()

s = 0
for i in numbers:
    s += int(i)
print(s)