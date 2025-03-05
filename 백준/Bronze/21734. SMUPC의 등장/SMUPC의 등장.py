for c in input():
    a = ord(c)
    q = sum(int(d) for d in str(a))
    print(c * q)
