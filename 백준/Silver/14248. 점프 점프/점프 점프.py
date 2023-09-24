N = int(input())
L = list(map(int, input().split()))
s = int(input()) - 1 
q = [s]
visited = [0 for _ in range(N)]
visited[s] = 1
answer = 1
while q:
    x = q.pop(0)
    y = L[x]
    for w in [x-y, x+y]:
        if N > w >= 0 and not visited[w]:
            visited[w] = 1
            answer += 1
            q.append(w)
print(answer)
