def solution(park, routes):
    answer = []
    N, M = len(park), len(park[0])
    for n in range(N):
        for m in range(M):
            if park[n][m] == "S":
                x, y = n, m
                break
    direction = {
        "N" : (-1, 0),
        "S" : (1, 0),
        "W" : (0, -1),
        "E" : (0, 1)
    }
    for z in routes:
        d, n = z.split()  
        nx, ny = x, y
        dx, dy = direction.get(d)
        for _ in range(int(n)):
            nx += dx
            ny += dy
            if N > nx >= 0 and M > ny >= 0 and park[nx][ny] != "X":
                continue
            else:
                break
        else:
             x, y = nx, ny   
    
    return [x, y]