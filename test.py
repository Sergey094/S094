def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i

n = int(input())
x = even_numbers(n)
for i in x:
    print(i)