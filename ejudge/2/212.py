n = int(input())
arr = list(map(int, input().split()))[:n]

for i in range(n):
    arr[i] = arr[i] * arr[i]

print(*arr)