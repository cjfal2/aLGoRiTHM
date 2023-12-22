def x(n,t,p):
    hap=int(v[n][p]) if p % 2 else int("".join(v[n][p-1:p+1]))
    if int(v[n][t])+int(v[n][t+2])==hap:
        v[n][t-1]=v[n][p+1]="*"
        for k in range(t,p+1):
            v[n-1][k]=v[n+1][k]="*"
    else:
        v[n-1][t+2]=v[n][t+1]=v[n+1][t]="/"
        
N, M=map(int,input().split())
v=[list(input()) for _ in range(N*3)]
for i in range(1,3*N,3):
    for j in range(1,8*M,8):
        x(i,j,j+4) if v[i][j+5]=="." else x(i,j,j+5)
    for a in range(i-1,i+2):
        print(*v[a],sep="")
