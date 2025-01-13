import sys

n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    ans = 0
    if x % 2 == 0:
        ans += x // 2
    else:
        ans += x // 2 + 1
    if x % 6 == 0 or x % 6 == 4:
        ans += x // 3
    else:
        ans += x // 3 + 1
    print(ans)
