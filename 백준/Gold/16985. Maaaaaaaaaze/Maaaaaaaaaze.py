from collections import deque
from itertools import permutations


pan = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
temp = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
answer = 200


def bfs(board):
    global answer

    q = deque([(0, 0, 0, 0)])
    visited = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1
    while q:
        x, y, h, cnt = q.popleft()
        if (x, y, h) == (4, 4, 4):
            answer = min(answer, cnt)
            if answer == 12:
                print(answer)
                quit()
            return

        if cnt >= answer:
            return

        for dx, dy, dh in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            nx, ny, nh = x + dx, y + dy, h + dh
            if 5 > nx >= 0 and 5 > ny >= 0 and 5 > nh >= 0 and board[nx][ny][nh] and not visited[nx][ny][nh]:
                q.append((nx, ny, nh, cnt + 1))
                visited[nx][ny][nh] = 1


def dfs(n):
    global temp

    if n == 5:
        if temp[4][4][4]:
            bfs(temp)
        return

    for _ in range(4):
        if temp[0][0][0]:
            dfs(n + 1)
        temp[n] = list(map(list, zip(*temp[n][::-1])))


for permu in permutations(list(range(5))):
    for i in range(5):
        temp[permu[i]] = pan[i]
    dfs(0)


print(answer if answer != 200 else -1)
