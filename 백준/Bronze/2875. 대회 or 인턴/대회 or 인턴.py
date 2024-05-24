g, m, t = map(int, input().split())
n = m
a = 0
for k in range(m):
    if n < 1 or g < 2:
        break
    else:
        g -= 2
        n -= 1
        a += 1
if g or n:
    for _ in range(g):
        if t:
            t -= 1
    for _ in range(n):
        if t:
            t -= 1
while t:
    a -= 1
    for i in range(3):
        if t:
            t -= 1
print(a)