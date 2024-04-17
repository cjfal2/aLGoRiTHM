def fibonacci(n):
    F = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] + F[0][1] * M[1][0]) % 1000000007
    y = (F[0][0] * M[0][1] + F[0][1] * M[1][1]) % 1000000007
    z = (F[1][0] * M[0][0] + F[1][1] * M[1][0]) % 1000000007
    w = (F[1][0] * M[0][1] + F[1][1] * M[1][1]) % 1000000007
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(PF, pn):
    if pn == 0 or pn == 1:
        return
    M = [[1, 1], [1, 0]]
    power(PF, pn // 2)
    multiply(PF, PF)
    if pn % 2 != 0:
        multiply(PF, M)


print(fibonacci(int(input())))
