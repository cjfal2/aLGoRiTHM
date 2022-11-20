MIN = 999999999999
co = 0
for _ in range(7):
    a = int(input())
    if a%2:
        co += a
        MIN = min(a, MIN)
if co:
    print(co)
    print(MIN)
else:
    print(-1)