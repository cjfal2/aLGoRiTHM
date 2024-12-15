n = int(input())
dp = [0 for _ in range(n+5)]  # 0: CY 승리, 1: SK 승리
# 초기값 설정
dp[1], dp[2], dp[3], dp[4] = 0, 1, 0, 1

for i in range(5, n + 1):
    dp[i] = 1 if dp[i - 1] == 0 or dp[i - 3] == 0 or dp[i - 4] == 0 else 0

print("SK" if dp[n] == 1 else "CY")
