from itertools import combinations

import sys
input = sys.stdin.readline

def find():
    for i in range(N):
        for j in range(N):
            if L[i][j] == 1:
                where_1.append((i, j))
            elif L[i][j] == 2:
                where_2.append((i, j))

def distance(home, bbq):
    return abs(home[0] - bbq[0]) + abs(home[1] - bbq[1])


N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

where_1 = []
where_2 = []
find()

temp = 999999
for bbq in list(combinations(where_2, M)):
    yogiyo = 0
    for home in where_1:
        MIN = 999999
        for zumpo in bbq:
            A = distance(home, zumpo)
            if MIN > A:
                MIN = A
        yogiyo += MIN
    if temp > yogiyo:
        temp = yogiyo
print(temp)