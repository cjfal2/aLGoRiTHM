words = input()
memo = set()
N = len(words)
visited = [0 for _ in range(N)]
x = []

def dfs(s):
    if len(s) == N:
        ss = "".join(s)
        if ss not in memo:
            memo.add(ss)
        return

    for i in range(N):
        if not visited[i]:
            if not s or s[-1] != words[i]:
                visited[i] = 1
                s.append(words[i])
                dfs(s)
                s.pop()
                visited[i] = 0
            

dfs(x)
print(len(memo))