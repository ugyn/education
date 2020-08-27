dna = input()

res = dna[0]
count = 0
for i in dna:
    if res != i:
        print(res + str(count), end = '')
        count = 0
        res = i
    count += 1
print(res + str(count))