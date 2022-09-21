# import sys
# sys.stdin = open("s1.txt", 'r')

pat = {
    "0001101": 0,
    "0011001": 1,
    "0010011": 2,
    "0111101": 3,
    "0100011": 4,
    "0110001": 5,
    "0101111": 6,
    "0111011": 7,
    "0110111": 8,
    "0001011": 9,
}
for tc in range(int(input())):
    garo, sero = map(int, input().split())
    barcord = [input().rstrip("0")[::-1] for _ in range(garo)]

    for bar in barcord:
        if '1' in bar:
            barcord1 = bar
            break
    # print(barcord1)
    
    barcord2 = list(barcord1)

    Q = []
    I = []
    while barcord2:
        I.append(barcord2.pop(0))
        if len(I)==7:
            Q.append(I)
            I = []
            if '1' not in barcord2:
                break
    # print(Q)

    real = ''
    for r in Q[::-1]:
        real += ''.join(r[::-1])
    # print(real)

    ans = []
    m = 0
    while m < len(real):
        if real[m:m+7] in pat:
            ans.append(pat.get(real[m:m+7]))
            m += 7
        else:
            m += 1

    zzak = 0
    hol  = 0   
    for idx, a in enumerate(ans):
        if idx%2:
            hol += a
        else:
            zzak += (a*3)
            
    if (zzak + hol)%10:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} {sum(ans)}')