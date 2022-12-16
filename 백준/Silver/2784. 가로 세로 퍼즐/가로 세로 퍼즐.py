from itertools import permutations
from copy import deepcopy

L = list(input() for _ in range(6))
for perm in permutations(L, 3):
    LL = deepcopy(L)
    for word in perm:
        LL.remove(word)
    sero = [
        perm[0][0]+perm[1][0]+perm[2][0],
        perm[0][1]+perm[1][1]+perm[2][1],
        perm[0][2]+perm[1][2]+perm[2][2],
    ]
    # print('perm',perm)
    # print('LL',LL)
    # print('sero',sero)
    # print("========")
    for r in LL:
        if r in sero:
            sero.remove(r)
    if not sero:
        for v in perm:
            print(v)
        quit()
print(0)