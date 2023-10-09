from itertools import combinations


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
answer = float("INF")

for start in combinations(list(range(N)), N//2):
    link = []
    for s in range(N):
        if s not in start:
            link.append(s)

    t, k = 0, 0
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            t += pan[start[i]][start[j]] + pan[start[j]][start[i]]
            k += pan[link[i]][link[j]] + pan[link[j]][link[i]]
            
    answer = min(answer, abs(t-k))

print(answer)
