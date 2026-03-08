import re

s = input()

d = re.search("cat|dog", s)

print("Yes" if d else "No")