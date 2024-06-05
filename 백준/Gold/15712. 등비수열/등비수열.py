def solve(r, n, m):
    if n == 1:
        return r % m
    if n == 0:
        return 1
    if n % 2:
        return ((r % m) * solve(r, n - 1, m)) % m
    else:
        temp = solve(r, n / 2, m)
        return (temp * temp) % m


def recur(r, n, m):
    if n == 1:
        return 1
    if n % 2:
        return ((recur(r, n // 2, m) * (1 + solve(r, n // 2, m))) % m + solve(r, n - 1, m)) % m
    else:
        return (recur(r, n // 2, m) * (1 + solve(r, n // 2, m))) % m


a, r, n, m = map(int, input().split())
print((a * recur(r, n, m)) % m)
