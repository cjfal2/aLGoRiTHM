import sys
input = sys.stdin.readline

Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

# 베시의 이동 시간 (대각선 이동 가능)
bessie_time = max(abs(Jr - Br), abs(Jc - Bc))

# 데이지의 이동 시간 (상하좌우 이동만 가능)
daisy_time = abs(Jr - Dr) + abs(Jc - Dc)

if bessie_time < daisy_time:
    print("bessie")
elif bessie_time > daisy_time:
    print("daisy")
else:
    print("tie")
