# def dfs(start):
#     global ans
#     if sum(s) >= B:
#         if ans > sum(s)-B:
#             ans = sum(s)-B
#     for i in range(start, N):
#         s.append(L[i])
#         dfs(i)
#         s.pop()
#
#
# for tc in range(int(input())):
#     N, B = map(int, input().split())
#     L = list(map(int, input().split()))
#     ans = 10000000000
#     s = []
#     dfs(0)
#     print(f'#{tc + 1} {ans}')
# ---------------------------------------------------
# from itertools import combinations
#
#
# for tc in range(int(input())):
#     N, B = map(int, input().split())
#     L = list(map(int, input().split()))
#     ans = 10000000000
#     for i in range(1, N+1):
#         S = list(combinations(L, i))
#         for s in S:
#             if sum(s) >= B:
#                 if ans > sum(s)-B:
#                     ans = sum(s)-B
#     print(f'#{tc+1} {ans}')
# ---------------------------------------------------
for tc in range(int(input())):
    N, B = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 10000000000
    for i in range(1 << N):
        s = []
        for j in range(N):
            if i & (1 << j):
                s.append(L[j])
        if sum(s) >= B:
            if ans > sum(s)-B:
                ans = sum(s)-B
    print(f'#{tc+1} {ans}')
