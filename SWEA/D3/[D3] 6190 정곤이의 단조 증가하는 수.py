for tc in range(int(input())):
    N = int(input())
    L = list(map(int,input().split()))
    Q = []
    for i in range(N-1):
        for j in range(i+1,N):
            Q.append(L[i]*L[j])
    if Q==[]:
        print(f'#{tc+1} -1')
    else:    
        danzo = []
        for x in Q:
            if x//10 == 0 and x!=10:
                danzo.append(x)
            else:    
                P = list(map(int,str(x)))
                J = ''
                G = False
                for p in range(len(P)-1):
                    if P[p] > P[p+1]:
                        J = ''
                        G = True
                        break
                    if G == False:
                        J+=str(P[p])
                if G == False:
                    J+=str(P[-1])
                    danzo.append(int(J))
        if danzo == []:
            print(f'#{tc+1} -1')
        else:
            print(f'#{tc+1} {max(danzo)}')