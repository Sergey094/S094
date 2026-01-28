a, s = int(input()), 0
n = list(map(int, input().split()))[:a]
print(n.index(max(n))+1)