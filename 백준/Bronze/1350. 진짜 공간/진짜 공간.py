def solve(a, b):
    c = 0
    for s in a:
        d = (s + b - 1) // b
        c += d * b
    return c


N = int(input())
print(solve(list(map(int, input().split())), int(input())))
