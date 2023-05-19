import sys
input = sys.stdin.readline

L = 0
N = int(input().strip())
for i in range(N):
    k = int(input().strip())
    if i == N-1:
        L += k
        continue
    L += k -1
print(L)