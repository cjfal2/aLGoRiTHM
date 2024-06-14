from collections import deque


N, M = map(int, input().split())
targets = deque(map(int, input().split()))
answer = 0
queue = deque(range(1, N + 1))

for target in targets:
    # 현재 큐에서 target의 위치 찾기
    idx = queue.index(target)
    # 왼쪽으로 이동하는 경우와 오른쪽으로 이동하는 경우 중 더 적은 연산 횟수 선택
    answer += min(idx, len(queue) - idx)
    # target을 뽑아내고 큐에서 제거
    queue.rotate(-idx)  # 왼쪽으로 idx만큼 회전
    queue.popleft()

print(answer)
