def reverse(st):
    st = st.split()
    st.reverse()
    s2 = ""
    for i in st:
        s2 += i + ' '
    return s2.strip()