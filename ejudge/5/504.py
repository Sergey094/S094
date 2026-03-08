import re

s = input()
d = re.findall("[0-9]", s)

for i in d:
    print(i, end = " ")