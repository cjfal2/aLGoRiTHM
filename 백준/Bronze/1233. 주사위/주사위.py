A, B, C = map(int, input().split())
answer = [0 for _ in range(A+B+C+1)]
for a in range(1, A+1):
    for b in range(1, B+1):
        for c in range(1, C+1):
            answer[a+b+c] += 1
print(answer.index(max(answer)))