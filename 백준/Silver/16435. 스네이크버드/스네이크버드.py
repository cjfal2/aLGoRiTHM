n, m = map(int, input().split())
for a in sorted(map(int, input().split())):
    if a <= m:
        m += 1
    else:
        break
print(m)
