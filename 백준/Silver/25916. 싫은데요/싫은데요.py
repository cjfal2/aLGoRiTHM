N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right, hap, answer = 0, 0, arr[0], 0

while right < N:
    if hap <= M:
        answer = max(answer, hap)
        right += 1
        if right < N:
            hap += arr[right]
            
    elif hap > M:
        hap -= arr[left]
        left += 1

print(answer)
