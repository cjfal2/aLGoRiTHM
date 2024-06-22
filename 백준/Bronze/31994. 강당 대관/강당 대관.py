a, b = "", 0
for _ in range(7):
    c, d = input().split()
    d = int(d)
    if d > b:
        a = c
        b = d
print(a)
        