import sys
input = sys.stdin.readline

n, m = map(int, input().split())
winds = [tuple(map(int, input().split())) for _ in range(n)]
queries = [int(input()) for _ in range(m)]

for q in queries:
    height = 0
    for l, r, x in winds:
        if l <= q <= r:
            if (q - l) % 2 == 0:
                height += x
            else:
                height -= x
    print(height)
