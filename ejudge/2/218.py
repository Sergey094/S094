n = int(input())
arr = [input() for _ in range(n)]

first_index = {}

for i, s in enumerate(arr, start=1):
    if s not in first_index:
        first_index[s] = i

for s in sorted(first_index):
    print(s, first_index[s])
