import re

s = input()
d = re.search("^[A-Z]|[a-z].*[0-9]$", s)

print("Yes" if d else "No")