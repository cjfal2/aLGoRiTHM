def move(pan, news):
    new = [[0 for _ in range(N)] for _ in range(N)]

    if news == 0:
        for i in range(N):
            temp = 0
            for j in range(N):
                if pan[i][j] != 0:
                    if new[i][temp] == 0:
                        new[i][temp] = pan[i][j]
                    elif new[i][temp] == pan[i][j]:
                        new[i][temp] *= 2
                        temp += 1
                    else:
                        temp += 1
                        new[i][temp] = pan[i][j]

    elif news == 1:
        for i in range(N):
            temp = N-1
            for j in range(N-1, -1, -1):
                if pan[i][j] != 0:
                    if new[i][temp] == 0:
                        new[i][temp] = pan[i][j]
                    elif new[i][temp] == pan[i][j]:
                        new[i][temp] *= 2
                        temp -= 1
                    else:
                        temp -= 1
                        new[i][temp] = pan[i][j]

    elif news == 2:
        for j in range(N):
            temp = 0
            for i in range(N):
                if pan[i][j] != 0:
                    if new[temp][j] == 0:
                        new[temp][j] = pan[i][j]
                    elif new[temp][j] == pan[i][j]:
                        new[temp][j] *= 2
                        temp += 1
                    else:
                        temp += 1
                        new[temp][j] = pan[i][j]

    elif news == 3:
        for j in range(N):
            temp = N-1
            for i in range(N-1, -1, -1):
                if pan[i][j] != 0:
                    if new[temp][j] == 0:
                        new[temp][j] = pan[i][j]
                    elif new[temp][j] == pan[i][j]:
                        new[temp][j] *= 2
                        temp -= 1
                    else:
                        temp -= 1
                        new[temp][j] = pan[i][j]

    return new


def dfs(pan, cnt):
    global ans
    if cnt == 5: # 최대 5번, 최대 크기 저장
        for i in range(len(pan)):
            for j in range(len(pan)):
                ans = max(ans, pan[i][j])
        return

    for news in (0, 1, 2, 3): # 좌 우 상 하
        new = move(pan, news)
        if new != pan:
            dfs(new, cnt + 1)
        else:
            for i in range(len(pan)):
                for j in range(len(pan)):
                    ans = max(ans, pan[i][j])
           

N = int(input())
if N==1:
    print(int(input()))
    quit()

pan = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dfs(pan, 0)
print(ans)
