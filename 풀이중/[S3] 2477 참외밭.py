K = int(input())
Q = [[],[],[],[],[],[]] #동1서2남3북4
for i in range(6):
    A,B=map(int,input().split())
    Q[i] += [A,B]
print(Q)

sem = [[],[],[],[],[]]





Pf = [] # 꺾인 곳1
Pb = [] # 꺾인 곳2
G = [] # 평평한 곳1
front = True
for q in Q:
    if len(q)==1:
        G.append(q[0])
        front = False
    elif front:
        Pf.append(q[0])
    else:
        Pb.append(q[0])

P = Pb+Pf
W = P[1:-1]

print(G)
print(Pf)
print(Pb)
print(P)
print(W)
# mini = W[0][0]*W[1][0]
# big =  G[0][0]*G[1][0]

# print(big,mini)
# print(K*(big-mini))