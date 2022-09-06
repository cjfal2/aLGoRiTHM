def combi(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next1 in combi(arr[i+1:], n-1):
                yield [arr[i]] + next1


N, M = map(int, input().split())
L = list(range(1, N+1))

Q = []
for num in combi(L, M):
    print(*num)
