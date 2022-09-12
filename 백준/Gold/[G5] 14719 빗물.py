sero, garo = map(int, input().split())
L = list(map(int, input().split()))
s = []
v = 0
for h in range(garo):
    while s and L[h] > L[s[-1]]:
        top = s.pop()
        if len(s) == 0:
            break
        d = h - s[-1] - 1
        w = min(L[h], L[s[-1]]) - L[top]
        v += (d * w)
    s.append(h)
print(v)
