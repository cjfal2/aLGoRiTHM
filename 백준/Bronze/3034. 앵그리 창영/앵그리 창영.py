N, garo, sero = map(int, input().split())
for _ in range(N):
    print("DA" if int(input()) ** 2 <= garo**2 + sero**2 else "NE")
