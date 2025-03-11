X, L, R = map(int, input().split())
if L <= X <= R:
    print(X)
else:
    print(L if abs(X - L) < abs(X - R) else R)
