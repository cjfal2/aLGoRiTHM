import sys
input = sys.stdin.readline

def to_index(c):
    return ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26

g, s_len = map(int, input().split())
W = input().strip()
S = input().strip()

from collections import defaultdict

target_count = [0] * 52
window_count = [0] * 52

# Step 1: 타겟 빈도 계산
for ch in W:
    target_count[to_index(ch)] += 1

# Step 2: 첫 슬라이딩 윈도우 초기화
for i in range(g):
    window_count[to_index(S[i])] += 1

result = 0
# Step 3: 비교
if window_count == target_count:
    result += 1

# Step 4: 슬라이딩 윈도우
for i in range(g, s_len):
    window_count[to_index(S[i - g])] -= 1  # 윈도우 빠지는 문자
    window_count[to_index(S[i])] += 1      # 윈도우 새로 들어오는 문자
    if window_count == target_count:
        result += 1

print(result)
