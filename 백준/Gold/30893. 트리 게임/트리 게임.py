from collections import deque
import sys
sys.setrecursionlimit(10**6)

n, s, e = map(int, input().split())
vec = [[] for _ in range(n + 1)]
check = [False] * (n + 1)
check_dfs = [False] * (n + 1)
dist = 0
answer = "Second"

for _ in range(n - 1):
    a, b = map(int, input().split())
    vec[a].append(b)
    vec[b].append(a)


def bfs():
    global dist
    q = deque([(s, 0)])

    while q:
        x, time = q.popleft()

        if x == e:
            dist = time
            return

        for node in vec[x]:
            if not check[node]:
                check[node] = True
                q.append((node, time + 1))


def dfs(x, time):
    global answer
    if x == s:
        answer = "First"
        return
    if check_dfs[x]:
        return
    check_dfs[x] = True

    if dist % 2 == 1:
        if time % 2 == 0:
            if len(vec[x]) > 2:
                return
            else:
                for node in vec[x]:
                    if not check_dfs[node]:
                        dfs(node, time + 1)
        else:
            for node in vec[x]:
                dfs(node, time + 1)
    else:
        if time % 2 == 1:
            if len(vec[x]) > 2:
                return
            else:
                for node in vec[x]:
                    if not check_dfs[node]:
                        dfs(node, time + 1)
        else:
            for node in vec[x]:
                dfs(node, time + 1)


def solve():
    bfs()
    for node in vec[e]:
        dfs(node, 1)

    print(answer)


solve()
