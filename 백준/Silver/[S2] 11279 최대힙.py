import heapq, sys
input = sys.stdin.readline

L = []
for _ in range(int(input().strip())):
    a = int(input().strip()) * -1
    if not a:
        if not L:
            print(0)
        else:
            print(heapq.heappop(L) * -1)
    else:
        heapq.heappush(L, a)