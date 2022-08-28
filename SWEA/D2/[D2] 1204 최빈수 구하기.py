for _ in range(int(input())):
    tc = int(input())
    L = list(map(int, input().split()))
    Q = [0]*102
    for i in L:
        Q[i] += 1
    Q = Q[::-1]
    print(f'#{tc} {101-(Q.index(max(Q)))}')
