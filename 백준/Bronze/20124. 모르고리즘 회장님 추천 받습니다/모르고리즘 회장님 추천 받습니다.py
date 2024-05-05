a = []
for _ in range(int(input())):
    b, c = input().split()
    c = int(c) * -1
    a.append((c, b))
a.sort()
print(a[0][1])