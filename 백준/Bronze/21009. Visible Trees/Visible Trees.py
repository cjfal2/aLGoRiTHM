N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
answer = []
for m in range(N):
    score = 1
    MAX = pan[0][m]
    for n in range(1, N):
        if pan[n][m] > MAX:
            score += 1
            MAX = pan[n][m]
    answer.append(score)
print(*answer)
for n in range(N):
    score = 1
    MAX = pan[n][0]
    for m in range(1, N):
        if pan[n][m] > MAX:
            score += 1
            MAX = pan[n][m]
    print(score)