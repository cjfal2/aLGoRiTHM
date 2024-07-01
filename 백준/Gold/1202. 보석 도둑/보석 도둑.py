import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
info = sorted(list(map(int, input().split())) for _ in range(N))
bags = sorted(int(input()) for _ in range(K))

answer = 0
temp = []

for bag in bags:
    while info and info[0][0] <= bag:
        heapq.heappush(temp, -info[0][1])
        heapq.heappop(info)
    if temp:
        answer -= heapq.heappop(temp)
print(answer)
