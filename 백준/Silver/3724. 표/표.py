for _ in range(int(input())):
    M, N = map(int, input().split())
    arr = [1 for _ in range(M)]
    for n in range(N):
        temp = list(map(int, input().split()))
        for m in range(M):
            arr[m] *= temp[m]
    answer = 0
    big = -float("INF")
    for a in range(M):
        if arr[a] >= big: 
            answer = max(answer, a)
            big = arr[a]
    print(answer+1)