# Напишите программу, которая считывает целые числа с консоли по одному числу в строке.

# Для каждого введённого числа проверить:
# если число меньше 10, то пропускаем это число;
# если число больше 100, то прекращаем считывать числа;
# в остальных случаях вывести это число обратно на консоль в отдельной строке.

while True:
    n = int(input())

    if n < 10:
        continue
    elif n > 100:
        break
    print(n)