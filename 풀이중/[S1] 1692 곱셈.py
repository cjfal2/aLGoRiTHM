def gop(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return (a * a) % c

    else:
        if b % 2:
            return ((gop(a, b // 2, c) ** 2) * a) % c

        else:
            return (gop(a, b // 2, c) ** 2) % c


A, B, C = map(int, input().split())
print(gop(A, B, C))
