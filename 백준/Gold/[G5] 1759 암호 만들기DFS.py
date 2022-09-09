# from itertools import combinations
#
# L, C = map(int, input().split())
# M = sorted(list(input().split()))
# X = list(combinations(M, L))
# Q = []
# U = ['a', 'i', 'u', 'e', 'o']
# for i in X:
#     a = 0
#     z = 0
#     for j in i:
#         if j in U:
#             a += 1
#         else:
#             z += 1
#     if a >= 1 and z >= 2:
#         Q.append(i)
# for k in Q:
#     print(*k, sep="")

def dfs(start):
    if len(s) == L:
        a = 0
        r = 0
        for i in s:
            for j in i:
                if j in U:
                    a += 1
                else:
                    r += 1
        if a >= 1 and r >= 2:
            print(*s, sep="")
        return
    for z in range(start, C):
        if visited[z] == 1:
            continue
        visited[z] = 1
        s.append(M[z])
        dfs(z)
        s.pop()
        visited[z] = 0


U = ['a', 'i', 'u', 'e', 'o']
L, C = map(int, input().split())
M = sorted(list(input().split()))
visited = [0] * (C+1)
s = []
dfs(0)
