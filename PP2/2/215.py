n = int(input())
st = []

for i in range(n):
    name = input()
    if name not in st:
        st.append(name)

print(len(st))