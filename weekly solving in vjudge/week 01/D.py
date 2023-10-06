def is_matched(exp):
    st = []
    for e in exp:
        if e == '{':
            st.append('}')
        elif e == '[':
            st.append(']')
        elif e == '(':
            st.append(')')
        else:
            if st == [] or e != st[-1]:
                return False
            st.pop()
    return st == []


s = int(input().strip())
for i in range(s):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")
