from collections import deque

n = int(input())
balloons = list(map(int, input().split()))

dq = deque([(i + 1, balloons[i]) for i in range(n)])

result = []
while dq:
    idx, move = dq.popleft()  # 맨 앞 풍선 터뜨림
    result.append(idx)
    if dq:
        if move > 0:
            dq.rotate(-(move - 1))  # 오른쪽으로 이동
        else:
            dq.rotate(-move)  # 왼쪽으로 이동

print(*result)
