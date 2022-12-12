for tc in range(int(input())):
    def check():
        pan = []
        co = 0
        for x in range(8):
            ipt = list(input())
            pan.append(ipt)
            for p in ipt:
                if p == 'O':
                    co += 1
        if co != 8:
            print(f'#{tc+1} no')
            return
        for i in range(8):
            for j in range(8):
                if pan[i][j] == 'O':
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        ni, nj = i, j
                        while 1:
                            ni += di
                            nj += dj
                            if 8 > ni >= 0 and 8 > nj >= 0:
                                if pan[ni][nj] == 'O':
                                    print(f'#{tc+1} no')
                                    return
                            else:
                                break
                            
        print(f'#{tc+1} yes')
    check()    
