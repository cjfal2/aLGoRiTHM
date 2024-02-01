N = int(input())
answer = 0
i = 1
while N:
    if i <= N:
        N -= i
        i += 1
        answer += 1
    else:
        i = 1
print(answer)