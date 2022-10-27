import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pan = dict()
for _ in range(N+M):
    aa, bb = map(int, input().strip().split())
    pan[aa] = bb

visited = [False for _ in range(101)]

q = [(1, 0)]
visited[1] = True
while q:
    t, m = q.pop(0)
    if t == 100:
        print(m)
        quit()
    for i in [1,2,3,4,5,6]:
        a = t+i
        if a <= 100 and not visited[a]:
            b = pan.get(a)
            if b:
                if not visited[b]:
                    q.append((b, m+1))
            else:
                q.append((a, m+1))
                visited[a] = True
                