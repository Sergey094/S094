import re

s = input()
d = re.findall(r"\S+@\S+\.\S+", s)


if d:
    print(d[0])
else:
    print("No email")