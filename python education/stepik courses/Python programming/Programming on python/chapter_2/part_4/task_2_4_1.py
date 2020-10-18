s = input().lower()

gc = 'gc'
gc_count = 0

for i in s:
    if i in gc:
        gc_count += 1

gc_percentage = gc_count / len(s) * 100

print(gc_percentage)