import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())

L = [list(map(int, input().strip().split())) for _ in range(N)]
L.sort()

answer = []
heapq.heappush(answer, L[0][1])

for i in range(1, N):
    if L[i][0] < answer[0]: # 가장 빨리 끝나는 시간보다 다음 회의의 시작시간이 빠르면
        heapq.heappush(answer, L[i][1]) # 방을 하나 더 빌린다.
    else: # 회의실 돌려막기 가능한 경우
        heapq.heappop(answer) # 가장 빠른 시간 pop해 준 후 다음 회의를 push
        heapq.heappush(answer, L[i][1])

print(len(answer))