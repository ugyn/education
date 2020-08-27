# Выведите таблицу размером n \times nn×n, заполненную числами от 11 до n^2
# по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):

# Sample Input:

# 5
# Sample Output:

# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())

matrix = [[None] * n for _ in range(n)]

dx, dy = 0, 1
x, y = 0, 0
for i in range(1, n * n):
    matrix[x][y] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and not matrix[nx][ny]:
        x, y = nx, ny
    else:
        dx, dy = dy, -dx
        x, y = x + dx, y + dy
matrix[x][y] = n * n
    
for x in range(n):
    print(*matrix[x])