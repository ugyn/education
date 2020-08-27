#refactored

n = int(input())
base = 'программист'

if n % 10 == 1 and not n % 100 == 11:
    ending = ''
elif 1 < n % 10 < 5 and not 10 < n % 100 < 15:
    ending = 'а'
else:
    ending = 'ов'

print(n, base + ending)

#first

# n = int(input())
# base = 'программист'

# if n % 10 in [2, 3, 4] and not (n % 100 in [12, 13, 14]):
#     ending = 'а'
# elif n % 10 == 1 and n % 100 != 11:
#     ending = ''
# else:
#     ending = 'ов'

# print(n, base + ending)