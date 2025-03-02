import sys
from collections import deque

# 입력 받기
N, K = map(int, sys.stdin.readline().split())

# 1부터 N까지 큐 초기화
que = deque(range(1, N + 1))

while len(que) > 1:
    kp = que[0]  # 첫 번째 청설모 저장
    itercnt = min(K, len(que))  # 제거할 개수 결정
    
    for _ in range(itercnt):  
        que.popleft()  # K마리 제거
    
    que.append(kp)  # 첫 번째 청설모 다시 추가

# 마지막으로 남은 청설모 출력
print(que[0])
