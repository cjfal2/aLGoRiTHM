import sys
input = sys.stdin.readline

def cal(arr):
    temp = 0
    for k in range(4):
        if arr[0][k] != arr[1][k]:
            temp += 1
        if arr[0][k] != arr[2][k]:
            temp += 1
        if arr[2][k] != arr[1][k]:
            temp += 1
    return temp


def dfs(start):
    global ans
    if len(s) == 3:
        ans = min(ans, cal(s))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = 1
            s.append(L[i])
            dfs(i)
            s.pop()
            visited[i] = 0


for _ in range(int(input())):
    N = int(input())
    L = list(input().split())
    if N > 32:
        print(0)
        continue
    s = []
    ans = 99999999999
    visited = [0 for _ in range(N)]
    dfs(0)
    print(ans)