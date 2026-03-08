import re

s = input()

c = re.compile(r"\b\w+\b")

d = c.findall(s)
print(len(d))