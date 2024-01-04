D, K = map(int, input().split())
for i in range(1, K-1):
    memo = [0 for _ in range(D+2)]
    memo[1] = i
    for j in range(i, K-1):
        memo[2] = j
        for q in range(3, D+1):
            memo[q] = memo[q-1] + memo[q-2]
        if memo[D] == K:
            print(i)
            print(j)
            quit()