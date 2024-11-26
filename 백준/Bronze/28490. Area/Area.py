a = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    a = max(a, x*y)
print(a)