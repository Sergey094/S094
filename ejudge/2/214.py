n = int(input())
a = list(map(int, input().split()))

best = a[0]
best_count = 0

for x in a:
    count = a.count(x)
    if count > best_count or (count == best_count and x < best):
        best = x
        best_count = count

print(best)
