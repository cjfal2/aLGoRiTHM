from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
L = list(map(int, input().strip().split()))

tl = []
ts = set()
for i in L:
    # 순서랑 횟수를 알아야함

    if i not in ts:
        if len(tl) != N:
            tl.append([i, 1])
            ts.add(i)
        else:
            before = deepcopy(tl)
            before.sort(key=lambda x: x[1])
            a = tl.index(before[0])
            tl.pop(a)
            ts.discard(before[0][0])
            tl.append([i, 1])
            ts.add(i)
    else:
        for a in range(len(tl)):
            if tl[a][0] == i:
                tl[a] = [i, tl[a][1] + 1]
                break
for i, j in sorted(tl):
    print(i, end=' ')
