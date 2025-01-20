answer = 0
for _ in range(int(input())):
    a, d, g = map(int, input().split())
    score = a * (d + g)
    if a == (d + g):
        score *= 2
    answer = max(score, answer)
print(answer)