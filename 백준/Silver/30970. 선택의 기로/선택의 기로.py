arr = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    arr.append((a, b))
A = sorted(arr, key = lambda x: (-x[0], x[1]))
print(*A[0], *A[1])
B = sorted(arr, key = lambda x: (x[1], -x[0]))
print(*B[0], *B[1])
