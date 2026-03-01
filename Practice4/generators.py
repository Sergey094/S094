def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input())

for sq in squares(n):
    print(sq)




def even_numbers(nn):
    for i in range(0, nn + 1, 2):
        yield i

nn = int(input())

first = True
for x in even_numbers(nn):
    if not first:
        print(',', end='')
    print(x, end='')
    first = False
print()