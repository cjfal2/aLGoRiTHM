import sys
input = sys.stdin.readline

N = int(input().rstrip())
L = []
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    L.append((a, b))
L.sort(key=lambda x: (x[1], x[0]))
C = [(0, 0)]
while L:
    a = L.pop(0)
    if a[0] >= C[-1][1]:
        C.append(a)
print(len(C)-1)