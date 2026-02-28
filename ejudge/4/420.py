g = 0

def outer():
    n = 0
    def inner():
        nonlocal n
        global g
        local_x = 0
        for cmd in commands:
            scope, val = cmd
            val = int(val)
            if scope == "global":
                g += val
            elif scope == "nonlocal":
                n += val
            elif scope == "local":
                local_x += val
        return n
    final_n = inner()
    return final_n

n = 0
commands = [input().split() for _ in range(int(input()))]

n = outer()
print(f"{g} {n}")