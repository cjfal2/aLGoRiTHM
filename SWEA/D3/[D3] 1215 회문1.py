for tc in range(10):
    M = int(input())
    pan = [list(input()) for _ in range(8)]
    pan_r = [[pan[i][j] for i in range(8)] for j in range(8)]
    co = 0
    for x in range(8):
        for y in range(9-M):
            A = pan[x][y:y+M]
            B = pan_r[x][y:y+M]
            if A == A[::-1]:
                co += 1
            if B == B[::-1]:
                co += 1
    print(f'#{tc+1} {co}')
