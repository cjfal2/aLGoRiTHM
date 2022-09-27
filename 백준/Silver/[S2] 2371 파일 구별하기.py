N = int(input())
L = [list(map(int, input().split()))[:-1] for _ in range(N)]
MAX = 0
for a in L:
    if MAX < len(a):
        MAX = len(a)

for b in range(N):
    if len(L[b]) < MAX:
        while len(L[b]) != MAX:
            L[b].append(0)
i = 0
while 1:
    i += 1
    temp = set()
    for c in L:
        temp.add(tuple(c[:i]))
    if len(list(temp)) == N:
        print(i)
        break

