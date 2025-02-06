import sys
input = sys.stdin.readline

N = int(input().strip())
temp = set()
res = []
arr = [list(input().strip().split()) for _ in range(N)]
arr.sort(key=lambda x: -int(x[1]))
for a in arr:
    A, B, C = a
    if C in temp:
        continue
    temp.add(C)
    res.append(A)

print(len(res))
for r in sorted(res):
    print(r)