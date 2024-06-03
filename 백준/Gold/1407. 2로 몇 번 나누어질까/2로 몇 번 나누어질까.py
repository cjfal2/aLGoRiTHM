def solve(a):
    result = a
    i = 2
    while i <= a:
        result += (a // i) * (i // 2)
        i *= 2
    return result

A, B = map(int, input().split())
print(solve(B) - solve(A - 1))
