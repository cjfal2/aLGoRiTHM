pibo = [0 for _ in range(1004)]
pibo[0] = pibo[1] = 1
for i in range(2, 1004):
    pibo[i] = pibo[i-1] + pibo[i-2]

while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    answer = 0
    for i in range(1, 1004):
        if b >= pibo[i] >= a:
            answer += 1

    print(answer)