from collections import deque


for tc in range(int(input())):
    N, K = map(int, input().split())
    L = deque()
    for k in input():
        L.append(k)
    temp = set()
    n = N//4
    for _ in range(n):
        res = ''
        for i in range(N):
            res += L[i]
            if len(res) == n:
                temp.add(res)
                res = ''
        L.append(L.popleft())
    Q = []
    for t in list(temp):
        Q.append(int(t, base=16))
    Q.sort(reverse=True)
    print(f'#{tc+1} {Q[K-1]}')
