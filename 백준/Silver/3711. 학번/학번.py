def solve(ids):
    m = 1
    while 1:
        remainders = set()
        is_unique = True
        for id in ids:
            remainder = id % m
            if remainder in remainders:
                is_unique = False
                break
            remainders.add(remainder)
        if is_unique:
            return m
        m += 1


for _ in range(int(input())):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    print(solve(arr))
