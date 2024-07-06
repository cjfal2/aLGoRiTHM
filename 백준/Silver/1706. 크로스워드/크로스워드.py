N, M = map(int, input().split())
pan = [input() for _ in range(N)]
words = []

garo = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    for m in range(M):
        if pan[n][m] != "#" and not garo[n][m]:
            word = pan[n][m]
            garo[n][m] = 1
            for k in range(m+1, M):
                if pan[n][k] != "#":
                    word += pan[n][k]
                    garo[n][k] = 1
                else:
                    break
            if len(word) > 1:
                words.append(word)
sero = [[0 for _ in range(M)] for _ in range(N)]
for m in range(M):
    for n in range(N):
        if pan[n][m] != "#" and not sero[n][m]:
            word = pan[n][m]
            sero[n][m] = 1
            for k in range(n+1, N):
                if pan[k][m] != "#":
                    word += pan[k][m]
                    sero[k][m] = 1
                else:
                    break
            if len(word) > 1:
                words.append(word)
print(sorted(words)[0])
