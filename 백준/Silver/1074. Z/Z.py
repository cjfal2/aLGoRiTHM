def Z(n, x, y):
    if n == 0:
        return 0
    return 2*(x%2)+(y%2) + 4*Z(n-1, x//2, y//2)

N, r, c = map(int, input().split())
print(Z(N, r, c))