# Напишите программу, которая считывает с клавиатуры два числа aa и bb, считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 33.

# В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12][−5;12]. Всего чисел, делящихся на 33, на этом отрезке 66: -3, 0, 3, 6, 9, 12−3,0,3,6,9,12. Их среднее арифметическое равно 4.54.5

# На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 33.

#first

a, b = int(input()), int(input())

#this while could be replaced with a += -a % 3
while a % 3 != 0:
    a += 1

s = 0
for i in range(a, b + 1, 3):
    if i % 3 == 0:
        s += i

print(s / ((b - a) // 3 + 1))

#cool

# a, b = int(input()), int(input())
# a += -a % 3 
# b -= b % 3
# print((a + b) / 2)

# mod(a,n) = a - {n * Floor(a/n)}

# The modulus is a mathematical operation, sometimes described as "clock arithmetic." I find that 
# describing it as simply a remainder is misleading and confusing because it masks the real reason it 
# is used so much in computer science. It really is used to wrap around cycles.

# Think of a clock: Suppose you look at a clock in "military" time, where the range of times goes from 
# 0:00 - 23.59. Now if you wanted something to happen every day at midnight, you would want the 
# current time mod 24 to be zero:

# if (hour % 24 == 0):

# You can think of all hours in history wrapping around a circle of 24 hours over and over and the 
# current hour of the day is that infinitely long number mod 24. It is a much more profound concept 
# than just a remainder, it is a mathematical way to deal with cycles and it is very important in 
# computer science. It is also used to wrap around arrays, allowing you to increase the index and use 
# the modulus to wrap back to the beginning after you reach the end of the array.