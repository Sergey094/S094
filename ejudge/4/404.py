def squares(b, e):
    for i in range(b, e + 1):
        yield i**2

b, e = map(int, input().split())

for s in squares(b, e):
    print(s, end = " ")