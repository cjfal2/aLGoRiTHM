def binary_search(A, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if A[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def long(arr):
    A = [0 for _ in range(N)]
    A[0] = arr[0]
    length = 1
    for i in range(1, N):
        if arr[i] < A[0]:
            A[0] = arr[i]
        elif arr[i] > A[length-1]:
            A[length] = arr[i]
            length += 1
        else:
            j = binary_search(A, 0, length-1, arr[i])
            A[j] = arr[i]
    return length


N = int(input())
L = list(map(int, input().split()))
print(N-long(L))
