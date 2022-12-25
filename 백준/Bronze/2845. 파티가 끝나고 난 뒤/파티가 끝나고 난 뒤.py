a,b=map(int,input().split())
L=list(map(int,input().split()))
K = []
for l in L:
    K.append(l-(a*b))
print(*K)