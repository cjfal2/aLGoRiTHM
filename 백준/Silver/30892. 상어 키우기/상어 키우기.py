import heapq

N, K, T = map(int, input().split())
arr = sorted(map(int, input().split()))

idx = 0
can_eat = []  # 잡아먹을 수 있는 상어를 저장할 리스트

# 잡아먹을 수 있는 상어를 우선순위 큐에 추가
while idx < N and arr[idx] < T:
    heapq.heappush(can_eat, -arr[idx])
    idx += 1

# 최대 K마리의 상어를 잡아먹음
for _ in range(K):
    if can_eat:
        e = -heapq.heappop(can_eat)  # 크기가 작은 상어부터 잡아먹음
        T += e  # 상어를 잡아먹은 크기만큼 몸집이 커짐
        while idx < N and arr[idx] < T:
            heapq.heappush(can_eat, -arr[idx])
            idx += 1
    else:
        break

print(T)
