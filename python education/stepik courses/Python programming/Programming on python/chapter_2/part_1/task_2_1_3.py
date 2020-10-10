# Сколько всего знаков * будет выведено после исполнения фрагмента программы:

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

stars = ''

i = 0
while i < 5:
    stars += '*'
    if i % 2 == 0:
        stars += '**'
    if i > 2:
        stars += '***'
    i = i + 1

print(len(stars))