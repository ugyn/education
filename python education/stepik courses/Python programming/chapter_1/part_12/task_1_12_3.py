x = float(input())
y = float(input())
operation = str(input())

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "pow":
    print(x ** y)
elif not y:
    print('Деление на 0!')
elif operation == "/":
    print(x / y)
elif operation == "mod":
    print(x % y)
elif operation == "div":
    print(x // y)