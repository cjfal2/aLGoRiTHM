for tc in range(int(input())):
    N,M=map(int,input().split())
    Q = input().split()
    for _ in range(M):
        Q.append(Q.pop(0))
    print(f'#{tc+1} {Q[0]}')