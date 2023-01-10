import sys
input = sys.stdin.readline


def dfs(arr):
    nxt = G[arr[-1]]
    if nxt == flag:
        real_arr.append(nxt)
        return
        
    if not memo[nxt]:
        memo[nxt] = 1
        arr.append(nxt)
        dfs(arr)
        arr.pop()
        memo[nxt] = 0
        

N = int(input().strip())

G = [0] + [int(input().strip()) for _ in range(N)] # 패딩줌
memo = [0 for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

real_arr = []
for k in range(1, N+1):
    if not visited[k]:
        flag = k
        dfs([k])


print(len(real_arr))
for i in sorted(real_arr):
    print(i)