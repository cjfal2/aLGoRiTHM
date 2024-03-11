def cal(num):
    t = []
    for n in (25, 10, 5, 1):
        a, num = divmod(num, n)
        t.append(a)
    return t


for _ in range(int(input())):
    print(*cal(int(input())))
