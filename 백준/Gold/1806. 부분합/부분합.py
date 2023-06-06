N, S = map(int, input().split())
L = list(map(int, input().split()))

ans = flag = 999999999999

start, end = 0, 0
now = L[0]

while start <= end < N:
    if now < S:
        end += 1
        if end == N:
            break
        now += L[end]
    else:
        ans = min(ans, end - start + 1)
        now -= L[start]
        start += 1

if ans == flag:
    print(0)
else:
    print(ans)
