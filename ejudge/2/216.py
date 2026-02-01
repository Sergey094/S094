n = int(input())
a = list(map(int, input().split()))
st = []

for i in a:
    if i in st:
        print("NO")
    else:
        print("YES")
        st.append(i)