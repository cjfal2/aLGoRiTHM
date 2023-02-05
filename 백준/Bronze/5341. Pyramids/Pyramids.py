while 1:
    n=int(input())
    if not n:
        break
    ans = 0
    for i in range(1,n+1):
        ans += i
    print(ans)