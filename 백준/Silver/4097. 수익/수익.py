import sys
input = sys.stdin.readline

while 1:
    N = int(input().strip())
    if not N:
        break
    MAX = -999999
    SUM = 0
    for _ in range(N):
        num = int(input().strip())
        if SUM + num > num:
            SUM = SUM + num
        else:
            SUM = num
        MAX = max(MAX, SUM)
    print(MAX)