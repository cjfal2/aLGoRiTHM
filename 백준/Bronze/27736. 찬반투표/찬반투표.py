o, x, d, N = 0, 0, 0, int(input())
S = N//2 + 1 if N % 2 else N//2
for i in map(int, input().split()):
    if i==1:
        o += 1
    elif i==0:
        d += 1
    else:
        x += 1
if d >= S:
    print("INVALID")
else:
    print("APPROVED") if o > x else print("REJECTED")
