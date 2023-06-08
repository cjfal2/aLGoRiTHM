N, M = map(int, input().split())
k = 0
where = []
for i in range(2500000):
    for j in range(4):
        k += 1
        if k == N or k == M:
            where.append((i, j))
    if len(where) == 2:
        break

print(abs(where[0][0]-where[1][0])+abs(where[0][1]-where[1][1]))
