N = int(input())
G = [0 for _ in range(N+1)]
for i in range(1, N+1):
    G[i] = int(input())
answer = 0
num = 0
for j in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    visited[j] = 1
    temp = 0
    q = j
    while 1:
        x = G[q]
        if visited[x]:
            if num < temp:
                num = temp
                answer = j
            break
        temp += 1
        visited[x] = 1
        q = x
print(answer)