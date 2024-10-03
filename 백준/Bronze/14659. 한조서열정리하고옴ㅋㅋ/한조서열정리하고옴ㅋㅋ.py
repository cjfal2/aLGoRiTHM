n=int(input())
arr = list(map(int, input().split()))
answer = 0
for i in range(n-1):
    number = arr[i]
    score = 0
    for j in range(i+1, n):
        target = arr[j]
        if number >= target:
            score += 1
        else:
            break
    answer = max(answer, score)
print(answer)