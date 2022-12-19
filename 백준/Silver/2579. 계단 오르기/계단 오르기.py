N = int(input())
if N == 0:
    print(0)
    quit()

stair = []
for _ in range (N):
    stair.append(int(input()))

if N == 1:
    print(stair[0])
    quit()
if N == 2:
    print(stair[0]+stair[1])
    quit()

memo = [0 for _ in range (N)]
memo[0] = stair[0]
memo[1] = max(stair[1], stair[0] + stair[1])
memo[2] = max(stair[0] + stair[2], stair[1] + stair[2])
for i in range(3, N):
    memo[i] = max(memo[i-2] + stair[i], memo[i-3] + stair[i-1] + stair[i])
    # max(직전 칸 최대, 전전 칸 최대)
print(memo[-1])
