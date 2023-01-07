import sys
input = sys.stdin.readline

N = int(input().strip())
W = [int(input().strip()) for _ in range(N)]

if N < 3:
    print(sum(W)) # 연속으로 마셔버리기
    quit()

memo = [0 for _ in range(N)] # 마신 최대를 저장할거
memo[0] = W[0]  # 처음
memo[1] = sum(W[:2]) # 두 번째 까지는 연속으로 2잔 마신게 제일 많이 마신거
memo[2] = max(W[0] + W[2], W[1] + W[2], memo[1]) # 연속으로 3잔 마시면 안되니까 최대를 저장

for i in range(3, N):
    memo[i] = max(
        memo[i - 3] + W[i - 1] + W[i],
        memo[i - 2] + W[i],
        memo[i - 1]
    )
        # 이전꺼랑 지금꺼 마신경우 최대 (3개 연속이면 안되니까)
        # 이전꺼 안마시고 지금꺼만 마신경우 최대
        # 지금꺼 안마신 경우 최대 (이전거랑 같음)

print(memo[-1])
