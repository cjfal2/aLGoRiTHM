def long(arr, n):
    L = [0] * n
    for i in range(n):
        L[i] = 1
        for j in range(0, i):
            if arr[j] < arr[i] and L[i] < L[j] + 1:
                L[i] = L[j] + 1
    return max(L)


N = int(input())
A = list(map(int, input().split()))
print(long(A, N))
