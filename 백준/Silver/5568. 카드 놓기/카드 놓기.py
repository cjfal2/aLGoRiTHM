N, K = int(input()), int(input())
L = [input() for _ in range(N)]
s = set()
memo = []
visited = [0 for _ in range(N)]

def back(n, cnt):
    global memo

    if cnt == K:
        s.add(n)
        return
    
    for i in range(N):
        if not visited[i]:
            memo.append(L[i])
            visited[i] = 1
            back("".join(memo), cnt+1)
            visited[i] = 0
            memo.pop()
back('', 0)
print(len(s))