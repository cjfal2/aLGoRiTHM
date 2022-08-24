bingo = [list(map(int,input().split())) for _ in range(5)]

zero = [0,0,0,0,0]

call = []
for _ in range(5):
    A = list(map(int,input().split()))
    for i in A:
        call.append(i)

z = -1
CHECK = 0
while z<23:
    check = 0

    z+=1
    for h in range(5):
        for w in range(5):
            if bingo[h][w] == call[z]:
                bingo[h][w] = 0
                check = 1
                break
        if check:
            break
    
    if z > 10:
        bingo_r = [[bingo[g][j] for g in range(5)] for j in range(5)]
        degak1 = []
        degak2 = []
        for i in range(5):
            degak1.append(bingo[i][i])
            degak2.append(bingo[i][4-i])

        degak1 = [degak1]
        degak2 = [degak2]
        
        hap = bingo+bingo_r+degak1+degak2
        
        if hap.count(zero) >= 3:
            CHECK = 1

    if CHECK==1:
        print(z+1)
        break