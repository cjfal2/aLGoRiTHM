for tc in range(int(input())):
    N,M=map(int,input().split())
    P = list(map(int,input().split()))
    Q = [] # 순서를 포함한 P의 요소를 만들어줌
    for idx,p in enumerate(P):
        Q.append([p,idx+1])
    # [[7,1],[2,2],[6,3],[5,4],[3,5]]

    C = [] # C는 화덕
    while len(C)!=1: # C의 요소가 1개이면 종료
        if Q: # Q에 아직 피자가 남았을 경우
            while len(C)!=N: # C가 꽉찰때까지 Q를 선입선출
                C.append(Q.pop(0))
        #---결국 Q의 요소가 1개남았을때도 C는 1개의 공간이 남아서
        #---오류가 나올 수 없다고 생각했다.(2번째 while문의 정상적 종료)

        A = C.pop(0) # C의 요소를 선입선출하고
        A[0]//=2 # 치즈를 절반으로 녹임
        if A[0]==0: # 0이면 꺼내고 (C에 공간이 남게됨)
            continue
        else: # 0이 아니면 다시 화덕에 넣어서 녹임
            C.append(A)
    print(f'#{tc+1} {C[0][1]}')