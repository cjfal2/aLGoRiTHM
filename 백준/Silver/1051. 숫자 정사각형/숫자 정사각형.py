N, M = map(int, input().split())
pan = [list(map(int, list(input()))) for _ in range(N)]
answer = 1
for n in range(N-1):
    for m in range(M-1):
        what = pan[n][m]
        for k in range(m+1, M):
            if pan[n][k] == what:
                if n+k-m < N and pan[n+k-m][m] == pan[n+k-m][k] == what:
                    answer = max(answer, (k-m+1)**2)
print(answer)