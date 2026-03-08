import re

s = input()

d = re.findall(r"\d{2,}", s)

print(" ".join(d))