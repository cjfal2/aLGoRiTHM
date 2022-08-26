for tc in range(int(input())):
    N,P = map(int,input().split())
    c = [N//P for _ in range(P)]
    for i in range(N%P):
        c[i]+=1
    x = 1
    for j in c:
        x*=j
    print(f'#{tc+1} {x}')