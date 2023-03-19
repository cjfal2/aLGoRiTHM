import sys
input = sys.stdin.readline

def dfs1(x):
    visited = set()
    visited.add(x)
    q = [x]
    while q:
        for w in G[q.pop()]:
            if w not in visited:
                q.append(w)
                visited.add(w)
    return visited
    

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
    a, b = map(int, input().strip().split())
    
    temp = dfs1(a)
    dfs2(b)
    