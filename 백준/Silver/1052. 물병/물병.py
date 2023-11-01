N, K = map(int, input().split())

answer = 0
while 1:
    cnt, temp = 0, N

    while temp:
        if temp % 2:
            cnt += 1
        temp //= 2
    
    if cnt <= K:
        print(answer)
        break
    
    answer += 1
    N += 1