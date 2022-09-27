# def dp(idx1, idx2, co):
#     global ans

#     if idx1 >= N:
#         ans = max(ans, co)
#         return
#     for i in [idx2, idx2+1]:
#         dp(idx1+1, i ,co+triangle[idx1][idx2])


# N = int(input())
# triangle = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# dp(0, 0, 0)
# print(ans)


N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            triangle[i][0] += triangle[i-1][0]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[N-1]))
