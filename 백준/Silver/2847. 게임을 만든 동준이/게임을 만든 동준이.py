N = int(input())
L = [int(input()) for _ in range(N)]
answer = 0
for i in range(N-2, -1, -1):
    while L[i+1] <= L[i]:
        L[i] -= 1
        answer += 1
print(answer)