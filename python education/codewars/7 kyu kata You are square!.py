def is_square(n):  
    if n < 0:
        return False
    else:
        return not bool(n ** 0.5 - int(n ** 0.5)) # If the square root is an integer, for example 3, then n ** 0.5 - int (n ** 0.5) will be 0 (False). If the square root was a real number of 3.2, then it will be True (any nonzero value).