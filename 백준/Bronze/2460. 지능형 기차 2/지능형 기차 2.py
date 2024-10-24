answer = 0
now = 0
for _ in range(10):
    i, j = map(int, input().split())
    now -= i
    now += j
    answer = max(answer, now)
print(answer)
