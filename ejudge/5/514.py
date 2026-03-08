import re

s = input()

d = re.compile(r"^\d+$")

if d.fullmatch(s):
    print("Match")
else:
    print("No match")