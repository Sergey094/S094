import re

s = input()

def di(d):
    return d.group() * 2

r = re.sub(r"\d", di, s)

print(r)