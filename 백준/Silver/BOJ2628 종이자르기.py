G, S = map(int,input().split())
N = int(input())

L = [[0,S],[0,G]] #[세로,가로] -> 세로로 자르면 가로가 영향받고, 가로로 자르면 세로가 영향받는다.
for _ in range(N):
    gs,num = map(int,input().split())
    L[gs] = L[gs] + [num]

Q = []
for i in L:
    Q.append(sorted(i))

X = []
for x in range(len(L[0])-1):
    for y in range(len(L[1])-1):
        s = Q[0][x+1]-Q[0][x]
        g = Q[1][y+1]-Q[1][y]
        X.append(s*g)

print(max(X))