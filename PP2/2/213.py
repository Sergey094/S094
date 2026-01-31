n = int(input())
s = 0

for i in range(n):
    if n % (i + 1) == 0:
        s += 1

if s > 2:
    print("No")
else:
    print("Yes")