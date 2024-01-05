def back(depth, x, y, movekan):
    global answer
    
    for a in pan:
        if "." in a:
            break 
    else:
        answer = min(answer, depth)
        return

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x, y
        visited = set()
        while 1:
            nx += dx
            ny += dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == ".":
                visited.add((nx, ny))
                pan[nx][ny] = "#"
                
            else:
                break
        
        if visited:
            back(depth+1, nx - dx, ny - dy, movekan + len(visited))
            for i, j in visited:
                pan[i][j] = "."
    

case = 0
while 1:
    try:
        case += 1
        answer = 9999999
        N, M = map(int, input().split())
        pan = [list(input()) for _ in range(N)]

        for n in range(N):
            for m in range(M):
                if pan[n][m] == ".":
                    pan[n][m] = "#"
                    back(0, n, m, 0)
                    pan[n][m] = "."

        if answer == 9999999:
            answer = -1
        print(f'Case {case}: {answer}')

    except:
        break