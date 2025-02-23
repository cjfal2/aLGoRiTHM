import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

len1, len2 = len(s1), len(s2)
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

max_length = 0  # 최장 공통 부분 문자열 길이 저장 변수

# DP 채우기
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if s1[i - 1] == s2[j - 1]:  # 같은 문자가 등장하면 이전 값 + 1
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])  # 최댓값 갱신

print(max_length)
