a, s = int(input()), 0
n = list(map(int, input().split()))
n = n[:a]
print(sum(1 for i in n if i > 0))