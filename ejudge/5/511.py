import re

s = input()

d = re.findall("[A-Z]", s)

print(len(d))