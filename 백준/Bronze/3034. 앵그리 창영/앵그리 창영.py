N, garo, sero = map(int, input().split())
daegak = garo**2 + sero**2

for _ in range(N):
    k = int(input())
    if k * k <= daegak:
        print("DA")
    else:
        print("NE")