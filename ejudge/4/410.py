def limited_cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

lst = input().split()
n = int(input())

first = True
for x in limited_cycle(lst, n):
    if not first:
        print(' ', end='')
    print(x, end='')
    first = False