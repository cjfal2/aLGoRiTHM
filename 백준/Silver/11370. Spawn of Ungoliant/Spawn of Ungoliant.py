import sys
input = sys.stdin.readline


while 1:
    M, N = map(int, input().strip().split())
    if N == M == 0:
        break
    pan = []
    flag = True
    
    for i in range(N):
        pp = list(input().strip())
        if flag:
            for j in range(M):
                if pp[j] == 'S':
                    sx, sy = i, j
                    flag = False
                    q = [(i, j)]
                    break
        pan.append(pp)
    
    while q:
        x, y = q.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == 'T':
                q.append((nx, ny))
                pan[nx][ny] = 'S'
    
    for v in pan:
        print(*v, sep='')
