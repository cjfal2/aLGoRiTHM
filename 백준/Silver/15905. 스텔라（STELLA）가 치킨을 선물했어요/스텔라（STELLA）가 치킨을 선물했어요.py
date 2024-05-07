n = int(input())
a = []
for _ in range(n):
    u, b = map(int, input().split())
    a.append((u, -b))
a.sort(reverse=1)
b = 0
c = a[4][0]
for i in range(5, n):
    if c == a[i][0]:
        b += 1
    else:
        break
print(b)
