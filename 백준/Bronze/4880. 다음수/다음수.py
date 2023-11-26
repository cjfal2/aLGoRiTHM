while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    e = b - a
    f = c - b
    if e == f:
        print("AP", c + e)
        continue
    e = b // a
    f = c // b
    print("GP", c * e)