import re

s = input()
w = input()

d = re.split(w, s)

print(",".join(d))