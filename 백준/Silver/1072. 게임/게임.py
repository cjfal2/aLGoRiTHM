import sys
input = sys.stdin.readline


X, Y = map(int, input().strip().split())
Z = (Y * 100) // X
if Z >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = X

    while left <= right:
        middle = (left + right) // 2
        if ((Y + middle) * 100) // (X + middle) <= Z:
            left = middle + 1
        else:
            answer = middle
            right = middle - 1

    print(answer)
