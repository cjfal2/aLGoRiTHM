def solution(n):
    a = ''
    while n > 0:
        n, mod = divmod(n, 3)
        a += str(mod)
    return int(a, 3)