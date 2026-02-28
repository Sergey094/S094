def numbers(n):
    for i in range(0, n + 1, 12):
        yield i

n = int(input())

for num in numbers(n):
    print(num, end = " ")