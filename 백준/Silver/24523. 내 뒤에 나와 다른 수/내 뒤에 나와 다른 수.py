N = int(input())
arr = list(map(int, input().split()))
answer = [-1 for _ in range(N)]


for i in range(N):
    a = arr[i]
    if i and arr[i-1] == a:
        answer[i] = answer[i-1]
        continue
    
    for j in range(i+1, N):
        b = arr[j]
        if a != b:
            answer[i] = j + 1
            break

print(*answer)
