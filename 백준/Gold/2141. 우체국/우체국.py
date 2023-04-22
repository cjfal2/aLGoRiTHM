import sys
input = sys.stdin.readline

N, L, hap = int(input().strip()), [], 0
for _ in range(N):
    a, b = map(int, input().strip().split())
    L.append((a, b))
    hap += b

L.sort()
temp = 0
for i in range(1, N+1):
    temp += L[i-1][1]
    if temp >= (hap+1)//2:
        print(L[i-1][0])
        break
