import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())

left = []  # 최대힙
right = [] # 최소힙
for _ in range(N):
    number = int(input().strip())
    
    heapq.heappush(left, -number) if len(left) == len(right) else heapq.heappush(right, number)
    # 힙큐에 left right 길이를 맞춰주며 넣어준다.

    if right and right[0] < -left[0]:
        # left 제일 큰거랑 right 제일 큰거랑 비교해서 left보다 right가 작다면 서로 바꿔준다.
        to_left = heapq.heappop(right)
        to_right = heapq.heappop(left)
        # 각각 최소힙, 최대힙에서 뽑아온 값이니 반대로 넣어줄 때 부호에 유의한다.
        heapq.heappush(left, -to_left)
        heapq.heappush(right, -to_right)

    print(-left[0]) # 출력은 항상 left의 최대힙값이다.
