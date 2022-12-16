N = int(input())
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x > (N+1)/2:
        x = N+1-x
    if y > (N+1)/2:
        y = N+1-y
    if x > y:
        ans = y%3
    else:
        ans = x%3
    if not ans:
        ans = 3
    print(ans)
    