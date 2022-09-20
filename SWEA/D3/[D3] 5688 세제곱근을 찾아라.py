for t in range(int(input())):
    N = int(input())
    if N == 1:
        num = 1
    else:
        for i in range(int(N ** (1 / 3)), N):
            if i**3 == N:
                num = i
                break
            elif i**3 > N:
                num = -1
                break
    print(f'#{t+1} {num}')
