# Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)

# Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.

# В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

#refactored

li = []
while True:
    i = input()
    if i == 'end':
        break
    li += [[int(x) for x in i.split()]]

n, m = len(li), len(li[0])

for i in range(n):
    for j in range(m):
        x = li[i - 1][j] + li[(i + 1) - n][j] + li[i][j - 1] + li[i][(j + 1) - m]
        print(x, end=' ')
    print()

#first

# li = []

# while True:
#     i = input()
#     if i == 'end':
#         break
#     li += [[int(x) for x in i.split()]]

# n = len(li)
# m = len(li[0])

# lo = [[0] * m for i in range(n)]

# for i in range(n):
#     for j in range(m):
#         lo[i][j] = li[i - 1][j] + li[(i + 1) % n][j] + li[i][j - 1] + li[i][(j + 1) % m]

# for i in range(n):
#     for j in range(m):
#         print(lo[i][j], end=' ')
#     print()