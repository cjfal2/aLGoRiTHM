N = int(input())
if N == 1:
    print(input())
    quit()

arr = [input() for _ in range(N)]
dif = set()
q = len(arr[0])

for a in range(N-1):
    for b in range(a, N):
        for c in range(q):
            if arr[a][c] != arr[b][c]:
                dif.add(c)
for k in range(q):
    if k not in dif:
        print(arr[0][k], end="")
    else:
        print("?", end="")