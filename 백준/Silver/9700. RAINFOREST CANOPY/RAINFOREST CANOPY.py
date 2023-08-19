import sys
input = sys.stdin.readline

tc = 0
while 1:
    try:
        N = int(input().strip())
        tc += 1
        pan = [list(map(int, list(input().strip()))) for _ in range(N)]
        answer = 0
        for n in range(N):
            for m in range(N):
                if pan[n][m]:
                    answer += 1
                    pan[n][m] = 0
                    q = [(n, m)]
                    while q:
                        x, y = q.pop(0)
                        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                            nx, ny = x + dx, y + dy
                            if N > nx >= 0 and N > ny >= 0 and pan[nx][ny]:
                                pan[nx][ny] = 0
                                q.append((nx, ny))
        print(f'Case #{tc}: {answer}')

    except:
        break