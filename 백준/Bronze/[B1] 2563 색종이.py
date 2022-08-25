base = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(int(input())):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            base[i][j]=1
co=0
for z in range(100):
    co+=base[z].count(1)
print(co)