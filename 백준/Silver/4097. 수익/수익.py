import sys
input = sys.stdin.readline


while 1:
    N = int(input().strip())
    if not N: break
    MAX, SUM = -99999, 0
    for _ in range(N):
        num = int(input().strip())
        SUM = SUM + num if SUM > 0 else num
        MAX = max(MAX, SUM)
    print(MAX)