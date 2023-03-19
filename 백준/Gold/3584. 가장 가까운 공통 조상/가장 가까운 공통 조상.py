import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

def dfs(x, arr):
    visited.add(x)
    for w in G[x]:
        if w not in visited:
            arr.append(w)
            dfs(w, arr)
    else:
        return arr
        

def check():
    for v in temp[0]:
        for h in temp[1]:
            if v == h:
                print(v)
                return

def dfs2(x):
    if x in temp:
        print(x)
        return
    visited = set()
    visited.add(x)
    q = [x]
    while q:
        for w in G[q.pop()]:
            if w not in visited:
                if w in temp:
                    print(w)
                    return
                else:
                    q.append(w)
                    visited.add(w)
            

for test_case in range(int(input().strip())):
    N = int(input().strip())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().strip().split())
        G[b].append(a)
    # print(G)
    a, b = map(int, input().strip().split())
    
    visited = set()
    temp = set(dfs(a, [a]))
    # print(temp)
    dfs2(b)
    