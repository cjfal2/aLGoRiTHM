for _ in range(int(input())):
    start, time = map(int, input().split())
    die = time // 7
    born = time // 4
    added = born - die
    print(start + added)