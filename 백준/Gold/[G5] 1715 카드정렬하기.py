import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
L = []
for _ in range(N):
    heapq.heappush(L, int(input().strip()))

ans = 0
while len(L) > 1:
    a = heapq.heappop(L)
    b = heapq.heappop(L)
    ans += a + b
    heapq.heappush(L, a+b)

print(ans)