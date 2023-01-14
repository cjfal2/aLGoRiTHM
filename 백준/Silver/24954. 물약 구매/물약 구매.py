def dfs():
    global ans
    if len(s) == N:
        total = 0
        boksa = C[:]
        for c in s:
            total += boksa[c]
            for p in P[c]:
                boksa[p[0]] -= p[1]
                if boksa[p[0]] <= 0:
                    boksa[p[0]] = 1
        ans = min(ans, total)
        return

    for j in range(1, N+1):
        if not visited[j]:
            visited[j] = 1
            s.append(j)
            dfs()
            s.pop()
            visited[j] = 0


N = int(input()) # 물약의 종류 N개
C = [0] + list(map(int, input().split())) # 물약의 가격
# 물약의 할인 정보 N개
P = dict()
for i in range(1, N+1):
    A = []
    for _ in range(int(input())):
        A.append(list(map(int, input().split())))
    P[i] = A

ans = 9999999999
s = []
visited = [0 for _ in range(N+1)]
dfs()
print(ans)
