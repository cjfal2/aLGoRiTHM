def solution(n):
    answer = []
    pan = [[0 for _ in range(n)] for _ in range(n)]
    last = 0
    for i in range(1, n+1):
        last += i
        
    # 하 우 대각
    direx = [1, 0, -1]
    direy = [0, 1, -1]
    
    direction = 0
    number = 1
    x, y = 0, 0
    while number < last + 1:
        pan[x][y] = number
        nx = x + direx[direction]
        ny = y + direy[direction]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or pan[nx][ny]:
            direction = (direction + 1) % 3
            nx = x + direx[direction]
            ny = y + direy[direction]
        x, y = nx, ny
        number += 1
    
    for a in pan:
        for b in a:
            if b:
                answer.append(b)
    
    return answer