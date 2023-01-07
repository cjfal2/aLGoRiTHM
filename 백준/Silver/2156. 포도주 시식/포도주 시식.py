import sys
input = sys.stdin.readline

N = int(input())
W = [int(input()) for _ in range(N)]
if N < 3:
    print(sum(W))
    quit()
def dp():
    memo = [0 for _ in range(N)]
    memo[0] = W[0]
    memo[1] = sum(W[:2])
    memo[2] = max(W[0] + W[2], W[1] + W[2], memo[1])

    for i in range(3, N):
        memo[i] = max(
            memo[i - 3] + W[i - 1] + W[i],
            memo[i - 2] + W[i],
            memo[i - 1]
        )
    print(memo[-1])
dp()