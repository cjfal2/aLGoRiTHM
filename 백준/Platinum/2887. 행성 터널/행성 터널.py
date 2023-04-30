import sys
input = sys.stdin.readline


def find(x):
    if rep[x] != x:
        rep[x] = find(rep[x])
    return rep[x]


def union(x, y):
    rep[find(x)] = find(y)


N = int(input().strip())
xyz = [[] for _ in range(3)]
edge = []
rep = [i for i in range(N)]

for i in range(N):
    x, y, z = map(int, input().strip().split())
    # (좌표, 행성번호)
    xyz[0].append((x, i))
    xyz[1].append((y, i))
    xyz[2].append((z, i))


for i in range(3):
    xyz[i].sort()
# 각 좌표를 가까운 비용 순으로 솔트

for i in range(N-1):
    for j in range(3):
        edge.append((abs(xyz[j][i][0] - xyz[j][i+1][0]), xyz[j][i][1], xyz[j][i+1][1]))
                    #      비용                          어디랑 어디를 이었는지

# MST
edge.sort()
ans = 0
for i in range(len(edge)):
    if find(edge[i][1]) != find(edge[i][2]):
        ans += edge[i][0]
        union(edge[i][1], edge[i][2])

print(ans)
