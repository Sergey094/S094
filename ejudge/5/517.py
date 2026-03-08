import re

s = input()

d = re.findall(r"\d{2}/\d{2}/\d{4}", s)

print(len(d))