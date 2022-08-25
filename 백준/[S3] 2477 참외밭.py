K = int(input())
Q = [[],[],[],[]] #동1서2남3북4
od = 0
for _ in range(6):
    od+=1 # 받는 순서
    A,B=map(int,input().split())
    Q[A-1]+=[[B,od]]

P = [] # 꺾인 곳
G = [] # 평평한 곳
for q in Q:
    if len(q)==2:
        P.append(q)
    else:
        G.append(q[0])
W = []
for p in P:
    W.append(p[0])
    W.append(p[1])
W.sort(key=lambda x:x[1])
W = W[1:-1]

mini = W[0][0]*W[1][0]
big =  G[0][0]*G[1][0]

print(big,mini)
print(K*(big-mini))