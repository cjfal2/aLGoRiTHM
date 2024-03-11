N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

answer = 0
for i in range(N-1):
    a, b = arr[i]
    temp = 0
    for j in range(i+1, N):
        c, d = arr[j]
        if a < c and d < b:
            temp += 1
    answer = max(answer, temp)
print(answer)