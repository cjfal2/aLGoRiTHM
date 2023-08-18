pan = int(input())
N = int(input())
M = int(input())

board = [input() for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

rooms = []
for n in range(N):
    for m in range(M):
        if not visited[n][m] and board[n][m] == ".":
            r = 1
            visited[n][m] = 1
            q = [(n, m)]
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and not visited[nx][ny] and board[nx][ny] == ".":
                        r += 1
                        q.append((nx, ny))
                        visited[nx][ny] = 1
            rooms.append(r)
            
rooms.sort()
answer = 0
while 1:
    x = rooms.pop()
    pan -= x
    if pan >= 0:
        answer += 1
    else:
        pan += x
        break

    if not rooms:
        break
print(f"{answer} rooms, {pan} square metre(s) left over") if answer != 1 else print(f"{answer} room, {pan} square metre(s) left over")