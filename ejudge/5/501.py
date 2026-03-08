import re

a = input()
b = re.search("^Hello.*$", a)

if b:
    print("Yes")
else:
    print("No")