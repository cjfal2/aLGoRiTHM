import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

# 변화량 배열 생성
diff = [0] * N
for i in range(1, N):
    diff[i] = abs(arr[i] - arr[i-1])

# 누적합 배열 생성
prefix = [0] * (N+1)
for i in range(1, N):
    prefix[i] = prefix[i-1] + diff[i]

# 질의 처리
for _ in range(Q):
    l, r = map(int, input().split())
    if r <= l:  # j-1 < i 인 경우
        print(0)
    else:
        print(prefix[r-1] - prefix[l-1])
