import json

def diff(a, b, path, res):
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a) | set(b)
        for k in keys:
            new_path = f"{path}.{k}" if path else k
            if k not in a:
                res.append((new_path, "<missing>", json.dumps(b[k], separators=(',', ':'))))
            elif k not in b:
                res.append((new_path, json.dumps(a[k], separators=(',', ':')), "<missing>"))
            else:
                diff(a[k], b[k], new_path, res)
    else:
        if a != b:
            res.append((
                path,
                json.dumps(a, separators=(',', ':')),
                json.dumps(b, separators=(',', ':'))
            ))

a = json.loads(input())
b = json.loads(input())

res = []
diff(a, b, "", res)

if not res:
    print("No differences")
else:
    for p, old, new in sorted(res):
        print(f"{p} : {old} -> {new}")