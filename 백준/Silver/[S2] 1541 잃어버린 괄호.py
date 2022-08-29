N = input()

if '-' in N and '+' in N:
    N = N.split('-')
    co = 0
    if '+' in N[0]:
        pq = 0
        H = N[0].split('+')
        for h in H:
            pq += int(h)
        co += pq
    else:
        co += int(N[0])

    for i in range(1, len(N)):
        if '+' in N[i]:
            pl = 0
            Q = N[i].split('+')
            for q in Q:
                pl += int(q)
            co -= pl
        else:
            co -= int(N[i])
elif '-' in N:
    N = N.split('-')
    co = int(N[0])
    for i in range(1, len(N)):
        co -= int(N[i])
elif '+' in N:
    N = N.split('+')
    co = int(N[0])
    for i in range(1, len(N)):
        co += int(N[i])
else:
    co = int(N)
print(co)
