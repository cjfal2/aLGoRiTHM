import sys
input = sys.stdin.readline

n=int(input().strip())
score = []
for _ in range(n):
    score.append(input().strip())
d, p = 0, 0
for w in score:
    if w == "D":
        d += 1
    else:
        p += 1
    if d != 0 and p != 0:
        if d >= p + 2 or p >= d + 2:
            print(f'{d}:{p}')
            quit()
print(f'{d}:{p}')