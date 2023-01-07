import sys
input=sys.stdin.readline
N=int(input())
W=[int(input()) for _ in range(N)]
if N<3:
    print(sum(W))
    quit()
def d():
    M=[0 for _ in range(N)]
    M[0]=W[0]
    M[1]=sum(W[:2])
    M[2]=max(W[0]+W[2],W[1]+W[2],M[1])
    for i in range(3,N):
        M[i] = max(
            M[i-3]+W[i-1]+W[i],
            M[i-2]+W[i],
            M[i-1]
        )
    print(M[-1])
d()