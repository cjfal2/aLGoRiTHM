sik = input()

sik = sik.split('-')
co = 0
if '+' in sik[0]:
    temp1 = 0
    H = sik[0].split('+')
    for h in H:
        temp1 += int(h)
    co += temp1
else:
    co += int(sik[0])

for i in range(1, len(sik)):
    if '+' in sik[i]:
        temp2 = 0
        Q = sik[i].split('+')
        for q in Q:
            temp2 += int(q)
        co -= temp2
    else:
        co -= int(sik[i])


# elif '-' in sik:
#     sik = sik.split('-')
#     co = int(sik[0])
#     for i in range(1, len(sik)):
#         co -= int(sik[i])


# elif '+' in sik:
#     sik = sik.split('+')
#     co = int(sik[0])
#     for i in range(1, len(sik)):
#         co += int(sik[i])


# else:
#     co = int(sik)
print(co)
