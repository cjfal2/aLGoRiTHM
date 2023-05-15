while 1:
    b, n = map(int, input().split())
    if not b:
        break
    d = []
    a = 0
    while 1:
        a += 1
        c = a ** n
        if c <= b:
            d.append(a)
        else:
            k = d[-1]**n
            ans = min(abs(b-k), abs(b-c))
            print(d[-1]) if ans == abs(b-k) else print(a)
            break