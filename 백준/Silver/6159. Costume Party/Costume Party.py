N, S = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
left = 0
right = N - 1
cnt = 0
while left < right:
    if arr[left] + arr[right] <= S:
        cnt += (right - left)
        left += 1
    else:
        right -= 1
print(cnt)
