import sys
from array import array

data = sys.stdin.buffer
n = int(data.readline())
pos = array('I', [0]) * (n + 1)  # 높이별 위치

# 입력 받은 높이의 위치를 저장
line = data.readline()
i = 0; num = 0; in_num = False
for ch in line:
    if 48 <= ch <= 57:  # 숫자
        in_num = True
        num = num * 10 + (ch - 48)
    else:
        if in_num:
            pos[num] = i
            i += 1
            num = 0
            in_num = False
if in_num:  # 마지막 숫자
    pos[num] = i

# 스윕 수 계산
cnt = 1
last = pos[n]
if n > 1:
    d = 1 if pos[n] < pos[n-1] else -1  # 1=좌→우, -1=우→좌
for v in range(n-1, 0, -1):
    p = pos[v]
    if (d == 1 and p > last) or (d == -1 and p < last):
        last = p
    else:
        cnt += 1
        last = p
        if v > 1:
            d = 1 if pos[v] < pos[v-1] else -1

print(cnt)
