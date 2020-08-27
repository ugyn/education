# Сколько итераций цикла будет выполнено в этом фрагменте программы?

# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2

count = 0

i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
        
    count += 1

print(count)