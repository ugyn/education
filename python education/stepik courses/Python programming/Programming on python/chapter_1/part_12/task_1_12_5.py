#refactored

a,b,c = int(input()), int(input()), int(input())

if a < b:
	a, b = b, a
if a < c:
	a, c = c, a
if b > c:
	b, c = c, b

print(a, b, c, sep='\n')

#first

# n1, n2, n3 = int(input()), int(input()), int(input())
# if n1 >= n2:
#     if n2 >= n3:
#         maximal = n1
#         average = n2
#         minimal = n3
#     elif n1 >= n3:
#         maximal = n1
#         average = n3
#         minimal = n2
#     else:
#         maximal = n3
#         average = n1
#         minimal = n2
# elif n2 >= n3:
#     maximal = n2
#     if n3 >= n1:
#         average = n3
#         minimal = n1
#     else:
#         average = n1
#         minimal = n3
# else:
#     maximal = n3
#     average = n2
#     minimal = n1
# print(maximal, minimal, average)