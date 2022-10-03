# prim (메모리 초과)
# def prim(start, V):
#     key = [BIG] * (V+1)
#     key[1] = 0
#     MST = [0] * (V+1)
#     pi = [0] * (V+1)

#     for _ in range(V):
#         u = 0
#         MIN = BIG

#         for i in range(1, V+1):
#             if MST[i] == 0:
#                 if key[i] < MIN:
#                     u = i
#                     MIN = key[i]
#         MST[u] = 1

#         for v in range(V+1):
#             if MST[v] == 0 and G[u][v] != 0:
#                 if key[v] > G[u][v]:
#                     key[v] = G[u][v]
#                     pi[v] = u
    
#     return sum(key[start:])



# V, E = map(int, input().split())
# BIG = 99999999

# G = [[0 for _ in range(V+1)] for _ in range(V+1)]

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     G[u][v] = w
#     G[v][u] = w

# print(prim(1, V))


# KRUSKAL, pypy 1400, python 시초
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

V, E = map(int, input().split())
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append((w, u, v))

edge.sort()

p = [i for i in range(V+1)]

N = V+1
cnt = 0
total = 0

for w, u, v in edge:
    if find_set(u) != find_set(v):
        cnt += 1
        total += w
        p[find_set(v)] = find_set(u)
        if cnt == V:
            break

print(p)
print(total)