import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, k, m = map(int, input().split())
    
    # 기본 불가능 체크
    if m != k + 1:
        print(-1)
        continue

    h = min(k, a - 1)  # 가능한 한 적게 가로 자르기
    v = k - h          # 나머지 세로 자르기

    # 가능한지 검증
    if v <= b - 1:
        print(h, v)
    else:
        print(-1)
