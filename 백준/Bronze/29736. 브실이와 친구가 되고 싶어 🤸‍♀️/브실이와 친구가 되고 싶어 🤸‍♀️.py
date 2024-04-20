A, B = map(int, input().split())
K, X = map(int, input().split())

answer = 0
for i in range(A, B+1):
    if abs(i - K) <= X:
        answer += 1

print(answer) if answer else print("IMPOSSIBLE")
