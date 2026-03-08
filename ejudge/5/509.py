import re

s = input()

d = re.findall(r"\b\w{3}\b", s)

print(len(d))