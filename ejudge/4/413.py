import json
import re

data = json.loads(input())
q = int(input())

token_re = re.compile(r'\.?([a-zA-Z_][a-zA-Z0-9_]*)|\[(\d+)\]')

for _ in range(q):
    query = input().strip()
    cur = data
    ok = True

    for name, idx in token_re.findall(query):
        if name:
            if isinstance(cur, dict) and name in cur:
                cur = cur[name]
            else:
                ok = False
                break
        else:
            i = int(idx)
            if isinstance(cur, list) and 0 <= i < len(cur):
                cur = cur[i]
            else:
                ok = False
                break

    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")