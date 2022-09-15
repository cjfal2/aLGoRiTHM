def bfs():
    visited = [[0 for _ in range(sero)] for _ in range(garo)]
    visited[men_x][men_y] = 1
    q = [[men_x, men_y]]
    while q:
        x, y = q.pop(0)
        a = chase[x][y]
        type_pipe = pipe.get(a)
        for dx, dy, dix in type_pipe:
            nx, ny = x + dx, y + dy
            if garo > nx >= 0 and sero > ny >= 0 and visited[nx][ny] == 0 and chase[nx][ny] != 0:
                if chase[nx][ny] in news.get(dix):
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    return visited


pipe = {
    1: [[-1, 0, 'n'], [1, 0, 's'], [0, -1, 'w'], [0, 1, 'e']],
    2: [[-1, 0, 'n'], [1, 0, 's']],
    3: [[0, -1, 'w'], [0, 1, 'e']],
    4: [[-1, 0, 'n'], [0, 1, 'e']],
    5: [[0, 1, 'e'], [1, 0, 's']],
    6: [[1, 0, 's'], [0, -1, 'w']],
    7: [[-1, 0, 'n'], [0, -1, 'w']]
}
news = {
    'n': [1, 2, 5, 6],
    'e': [1, 3, 6, 7],
    'w': [1, 3, 4, 5],
    's': [1, 2, 4, 7],
}
for tc in range(int(input())):
    garo, sero, men_x, men_y, move = map(int, input().split())
    chase = [list(map(int, input().split())) for _ in range(garo)]
    vis = bfs()
    co = 0
    for g in range(garo):
        for s in range(sero):
            if 0 < vis[g][s] <= move:
                co += 1
    print(f'#{tc+1} {co}')
