N = int(input())
arr = sorted(map(int, input().split()))
prev = arr[0]
score = arr[0]
for i in range(1, N):
    if prev + 1 == arr[i]:
        prev = arr[i]
        continue
    score += arr[i]
    prev = arr[i]
print(score)