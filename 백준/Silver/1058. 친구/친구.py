N = int(input())
G = [[] for _ in range(N)]
for n in range(N):
    temp = input()
    for t in range(n+1, N):
        if temp[t] == "Y":
            G[t].append(n)
            G[n].append(t)

A = [0 for _ in range(N)]
for a in range(N):
    f = 0
    for b in range(N):
        if a == b:
            continue
        if b in G[a]:
            f += 1
            continue
        for c in range(N):
            if a in G[c] and b in G[c]:
                f += 1
                break
    A[a] = f
print(max(A))
