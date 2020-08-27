#refactored

a, b, c = int(input()), int(input()), int(input())

p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(S)

#first

# from math import sqrt

# a, b, c = int(input()), int(input()), int(input())

# p = (a + b + c) / 2
# S = sqrt(p * (p - a) * (p - b) * (p - c))

# print(S)