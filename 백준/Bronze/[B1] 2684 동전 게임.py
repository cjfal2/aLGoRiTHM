CAN = ['TTT', 'TTH', 'THT', 'THH', 'HTT', 'HTH', 'HHT', 'HHH']
for tc in range(int(input())):
    L = input()
    q = [0] * 8
    for idx, c in enumerate(CAN):
        i = -1
        while i != 37:
            i += 1
            a = L[i]+L[i+1]+L[i+2]
            if c == a:
                q[idx] += 1
    print(*q)
