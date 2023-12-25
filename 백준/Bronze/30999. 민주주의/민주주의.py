n, m = map(int, input().split())
answer = 0
for _ in range(n):
    o, x = 0, 0
    for a in input():
        if a == "O":
            o += 1
        else:
            x += 1
    if o > x:
        answer += 1
print(answer)

