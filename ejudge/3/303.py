def summa(a):
    d = {
        "ZER": "0",
        "ONE": "1",
        "TWO": "2",
        "THR": "3",
        "FOU": "4",
        "FIV": "5",
        "SIX": "6",
        "SEV": "7",
        "EIG": "8",
        "NIN": "9"
    }

    rd = {v: k for k, v in d.items()}

    for op in ['+', '-', '*']:
        if op in a:
            left, right = a.split(op)
            oper = op
            break

    def conv(s):
        num = ""
        for i in range(0, len(s), 3):
            num += d[s[i:i+3]]
        return int(num)

    x = conv(left)
    y = conv(right)

    if oper == '+':
        res = x + y
    elif oper == '-':
        res = x - y
    else:
        res = x * y

    ans = ""
    for digit in str(res):
        ans += rd[digit]

    return ans


a = input().strip()
print(summa(a))
