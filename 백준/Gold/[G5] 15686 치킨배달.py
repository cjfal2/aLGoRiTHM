"""
대 시 간 초 과

def find():
    for i in range(N):
        for j in range(N):
            if L[i][j] == 1:
                where_1.append((i, j))
            elif L[i][j] == 2:
                where_2.append((i, j))

def distance(home, bbq):
    return abs(home[0] - bbq[0]) + abs(home[1] - bbq[1])


def choose():
    global temp

    if len(bbq) == M:
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
        return

    for i in range(len(where_2)):
        if where_2[i] in bbq:
            continue
        bbq.append(where_2[i])
        choose()
        bbq.pop()
        

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

where_1 = []
where_2 = []
find()

visited = [[0 for _ in range(N)] for _ in range(N)]

bbq = []
temp = 9999999
choose()
print(temp)
"""

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