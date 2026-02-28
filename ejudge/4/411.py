import json

def apply_patch(src, patch):
    for k, v in patch.items():
        if v is None:
            src.pop(k, None)
        elif k in src and isinstance(src[k], dict) and isinstance(v, dict):
            apply_patch(src[k], v)
            if src[k] == {}:
                src.pop(k, None)
        else:
            src[k] = v
    return src

source = json.loads(input())
patch = json.loads(input())

result = apply_patch(source, patch)

print(json.dumps(result, separators=(',', ':'), sort_keys=True))