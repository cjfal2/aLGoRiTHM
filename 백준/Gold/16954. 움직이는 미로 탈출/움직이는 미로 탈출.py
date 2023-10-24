'''
이동하려는데 벽인 경우 컷
이동했는데 위가 벽인 경우 컷
9방향 다 해보고 player에 넣은다음 벽이동시킴

벽이 없으면 1 무조건 -> 9초후에는 무조건 벽이 없어짐
벽이 플레이어의 n보다 낮아지면 무조건 1

'''

from collections import deque


def bfs():
    temp = '........'
    direc = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
    time = 0
    player = deque([(7, 0)])
    while player:
        visited = [[0 for _ in range(8)] for _ in range(8)]
        for _ in range(len(player)):
            x, y = player.popleft()
            if (x, y) == (0, 7):  # 탈출
                return 1

            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                if 8 > nx > 0 and 8 > ny >= 0 and not visited[nx][ny] and pan[nx][ny] != "#" and pan[nx-1][ny] != "#":
                    visited[nx][ny] = 1
                    player.append((nx, ny))

        pan.pop()
        pan.appendleft(temp)

        time += 1
        if time == 8:
            return 1 # 벽이 없어서 성공
    return 0  # 실패


pan = deque([input() for _ in range(8)])
print(bfs())
