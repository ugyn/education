def add_binary(a,b):
    sum = a + b
    l = []
    while sum != 0:
        l += [sum % 2] 
        sum = sum // 2    
    return ''.join(map(str, l[::-1]))