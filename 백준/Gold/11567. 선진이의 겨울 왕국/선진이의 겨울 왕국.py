def search_exit_bfs():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[sx][sy] = 1
    q = [(sx, sy)]
    before = (sx, sy)
    while q:
        x, y = q.pop(0)
        # print(x, y)
        if x == ex and y == ey:  # 탈출구 찾음
            if pan[x][y] == "X":
                print("YES")
                quit()
            else:
                can_exit(x, y, before)
                quit()

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny]:
                # 탈출구가 X인 경우 따로 조건 걸어둠
                if nx == ex and ny == ey and pan[nx][ny] == "X":
                    q.append((nx, ny))
                    visited[nx][ny] = 1

                if pan[nx][ny] == ".":
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    if nx == ex and ny == ey:
                        before = (x, y)


def can_exit(i, j, bf):
    '''
    주위 둘러보기
    '''
    for di, dj in (0, 1), (-1, 0), (1, 0), (0, -1):
        ni, nj = i + di, j + dj
        if (ni, nj) == bf:
            continue

        if N > ni >= 0 and M > nj >= 0 and pan[ni][nj] == ".":
            print("YES")
            break
    else:
        print("NO")


N, M = map(int, input().split())
pan = [list(input()) for _ in range(N)]
sx, sy = map(lambda x: int(x) - 1, input().split())
ex, ey = map(lambda x: int(x) - 1, input().split())

# 1. 시작 == 탈출구 인 경우 => 주위 점 1개라도 있으면 OK
if (sx, sy) == (ex, ey):
    can_exit(sx, sy, (-1, -1))
    quit()
    
# 2. 탈출구 == "X" 인경우 => 일반 BFS
# 3. 탈출구 == "." 인경우 => 주위 점 1개라도 있으면 OK
search_exit_bfs()  # 일반 BFS
print("NO")