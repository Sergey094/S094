import re

s = input()

d = re.findall(r"\w+", s)

print(len(d))