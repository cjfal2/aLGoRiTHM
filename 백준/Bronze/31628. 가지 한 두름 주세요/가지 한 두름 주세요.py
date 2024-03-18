def solve():
    pan1 = [input().split() for _ in range(10)]
    pan2 = list(map(list, zip(*pan1)))
    for i in range(10):
        if len(set(pan1[i])) == 1 or len(set(pan2[i])) == 1:
            return 1
    return 0


print(solve())
