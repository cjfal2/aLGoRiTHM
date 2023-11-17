a, b = map(int, input().split())
answer = 0
while 1:
    a -= 2
    b -= 1
    if a < 0 or b < 0:
        break
    answer += 1
print(answer)