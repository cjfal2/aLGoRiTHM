for _ in range(int(input())):
    co = 0
    MIN = 9999999999999
    for i in list(map(int, input().split())):
        if not i%2:
            co += i
            MIN = min(MIN, i)
    print(co, MIN)