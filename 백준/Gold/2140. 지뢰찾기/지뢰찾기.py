N=int(input())
p=[list(map(lambda x: int(x) if x != "#" else x,list(input()))) for _ in range(N)]
d=((1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1),(-1,1),(1,-1))
a=0 if N<=4 else (N-4)**2
for x in range(1,N-1):
    for y in range(1,N-1):
        if x in (1,N-2)or y in (1,N-2):
            for i,j in d:
                if p[x+i][y+j]==0:
                    break
            else:
                for i,j in d:
                    nx,ny=x+i,y+j
                    if p[nx][ny]!="#":
                        p[nx][ny]-=1
                a+=1
print(a)
