N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
left, right = 0, 0
answer = max(arr) - min(arr)
while left < N-1:
    gap = arr[right] - arr[left]
    if gap >= M:
        answer = min(answer, gap)
        left += 1
    else:
        if N-1 > right:
            right += 1
        else:
            left += 1
print(answer)
