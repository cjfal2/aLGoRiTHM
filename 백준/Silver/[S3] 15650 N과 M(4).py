# from itertools import combinations
#
# n, m = list(map(int, input().split()))
# q = [list(range(1, n+1)) for _ in range(m)]
#
# s = sorted(list(set(list(combinations(q, m)))))
# for z in s:
#     print(*z)



# def dfs():
#     if len(s) == m:
#         t = s[:]
#         a = sorted(s)
#         if a not in q:
#             q.append(t)
#         return
#     for i in range(1, n + 1):
#         s.append(i)
#         dfs()
#         s.pop()
#
#
# n, m = list(map(int, input().split()))
# s = list()
# q = list()
# dfs()
# for z in q:
#     print(*z)



# def combi(arr, n):
#     for i in range(len(arr)):
#         if n == 1:
#             yield [arr[i]]
#         else:
#             for next1 in combi(arr[i+1:], n-1):
#                 yield [arr[i]] + next1
#
#
# N, M = map(int, input().split())
# L = list(range(1, N+1))
# L = sorted(L*M)
# Q = []
# for num in combi(L, M):
#     if num not in Q:
#         Q.append(num)
#         print(*num)


def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


n, m = map(int, input().split())
s = []
dfs(1)
