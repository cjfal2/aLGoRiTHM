def bishop(start):
    global ans
    if start == N:
        ans += 1
        return
    for i in range(N):
        for j in range(N):
            if check_degak_1[start+i] and check_degak_2[start-i+(N-1)] and pan[i][j]:
                L[start] = i
                pan[i][j] = check_degak_1[start+i] = check_degak_2[start-i+(N-1)] = 0
                bishop(start+1)
                pan[i][j] = check_degak_1[start+i] = check_degak_2[start-i+(N-1)] = 1


N = int(input())
L = [0] * N
pan = [list(map(int, input().split())) for _ in range(N)]
check_degak_1 = [1] * ((N*2)-1)   # /
check_degak_2 = [1] * ((N*2)-1)   # \
ans = 0
bishop(0)
print(ans)
