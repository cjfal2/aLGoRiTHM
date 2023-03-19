sik = input()

if '-' in sik and '+' in sik:
    sik = sik.split('-')
    co = 0
    if '+' in sik[0]:
        pq = 0
        H = sik[0].split('+')
        for h in H:
            pq += int(h)
        co += pq
    else:
        co += int(sik[0])

    for i in range(1, len(sik)):
        if '+' in sik[i]:
            pl = 0
            Q = sik[i].split('+')
            for q in Q:
                pl += int(q)
            co -= pl
        else:
            co -= int(sik[i])


elif '-' in sik:
    sik = sik.split('-')
    co = int(sik[0])
    for i in range(1, len(sik)):
        co -= int(sik[i])


elif '+' in sik:
    sik = sik.split('+')
    co = int(sik[0])
    for i in range(1, len(sik)):
        co += int(sik[i])

        
else:
    co = int(sik)
print(co)
