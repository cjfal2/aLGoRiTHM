import sys

input = sys.stdin.readline

to = {0: 0, 1: 0, 2: 2, 3: 3, 4: 1}
n = int(input().strip()) // 2
p = []

for _ in range(n):
    a, b, c, d = map(int, input().strip().split())
    a, c = to[a], to[c]
    x, y = a * 51 + b, c * 51 + d
    if a > 1:
        x += 51 - 2 * b
    if c > 1:
        y += 51 - 2 * d

    p.append((min(x, y), max(x, y)))

ans = 0
cross = [0] * n

for i in range(n):
    a, b = p[i]
    for j in range(n):
        c, d = p[j]
        if a < c < b < d:
            ans += 1
            cross[i] += 1
            cross[j] += 1

print(ans)
print(max(cross))
