for _ in range(int(input())):
    n = int(input())
    answer = []
    i = 0
    
    while n > 0:
        if n & 1 == 1:
            answer.append(i)
        n = n >> 1
        i += 1
    
    print(*answer)
