#first

shape = input()

if shape == 'треугольник':
    a, b, c = int(input()), int(input()), int(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif shape == 'квадрат':
    a, b = int(input()), int(input())
    S = a * b
elif shape == 'круг':
    r = int(input())
    pi = 3.14
    S = pi * r ** 2

print(S)