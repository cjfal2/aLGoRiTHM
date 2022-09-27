N, M = map(int, input().split())
# L = [list(map(int, input().split())) for _ in range(N)]

L = []
for _ in range(N):
    guganhap = []
    ggh = 0
    for num in list(map(int, input().split())) :
        ggh += num
        guganhap.append(ggh)
    L.append(guganhap)

for v in L:
    print(v)

# for _ in range(M):
#     a, b, c, d = map(int, input().split())
#     co = 0
#     for x in range(a-1, c):
#         for y in range(b-1, d):
#             co += L[x][y]
#     print(co)
