n = int(input())
db = {}

for _ in range(n):
    line = input()
    if line.startswith("set "):
        _, key, value = line.split(maxsplit=2)
        db[key] = value
    elif line.startswith("get "):
        _, key = line.split(maxsplit=1)
        if key in db:
            print(db[key])
        else:
            print(f"KE: no key {key} found in the document")
