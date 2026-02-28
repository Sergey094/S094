def gen(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())

for g in gen(n):
    print(g)