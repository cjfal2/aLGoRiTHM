def queen(start):
    global ans
    if start == N:
        ans += 1
        return
    for i in range(N):
        if not check_hang[i] and not check_degak_1[start+i] and not check_degak_2[start-i+(N-1)]:
            pan[start] = i
            check_hang[i] = check_degak_1[start+i] = check_degak_2[start-i+(N-1)] = 1
            queen(start+1)
            check_hang[i] = check_degak_1[start+i] = check_degak_2[start-i+(N-1)] = 0


N = int(input())
pan = [0] * N
check_hang = [0] * N    # ㅡ
check_degak_1 = [0] * ((N*2)-1)   # /
check_degak_2 = [0] * ((N*2)-1)   # \
ans = 0
queen(0)
print(ans)
