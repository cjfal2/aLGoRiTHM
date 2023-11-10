import sys
input = sys.stdin.readline


def find(a):
    if rep[a] != a:
        rep[a] = find(rep[a])
    return rep[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        rep[a] = b
    else:
        rep[b] = a


def is_connected(parent):
    root = find(0)
    for i in range(len(parent)):
        if find(i) != root:
            return False
    return True


N = int(input().strip())
rep = [i for i in range(N)]
edge = []

lan_code_length = 0
for u in range(N):
    arr = list(input())
    for v in range(N):

        d = arr[v]
        if d == "0":
            continue

        if d in "qwertyuiopasdfghjklzxcvbnm":
            d = ord(d) - 96
        else:
            d = ord(d) - 65 + 27

        lan_code_length += d

        if u == v:
            continue

        edge.append([d, u, v])
edge.sort()

total = 0
for d, u, v in edge:
    if find(u) != find(v):
        total += d
        union(u, v)

if is_connected(rep):
    print(lan_code_length - total)
else:
    print(-1)