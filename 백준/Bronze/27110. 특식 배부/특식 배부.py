N=int(input())
ans=0
for v in map(int,input().split()):
    if v<=N:
        ans+=v
    else:
        ans+=N
print(ans)