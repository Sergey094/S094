import re

s = input()
w = input()
p = input()

d = re.sub(w, p, s)

print(d)