import sys
input = sys.stdin.readline

N, chicken = map(int, input().split())
arr = [int(input()) for _ in range(N)]

left = 1
right = max(arr)

res = 0

while left <= right:
    mid = (left+right) // 2

    current_chicken = 0
    for green_onion in arr:
        current_chicken += green_onion // mid

    if current_chicken >= chicken:
        res = max(res, mid)
        left = mid+1
    else:
        right = mid - 1

print(sum(arr) - (chicken * res))
