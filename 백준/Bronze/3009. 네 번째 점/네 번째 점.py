a, b = [], []
for _ in range(3):
    c, d = map(int, input().split())
    a.append(c) if c not in a else a.remove(c)
    b.append(d) if d not in b else b.remove(d)
print(*a, *b)