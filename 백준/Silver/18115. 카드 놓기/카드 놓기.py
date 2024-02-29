from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])
answer = deque([])
for a in list(map(int, input().split()))[::-1]:
    b = cards.popleft()
    if a == 1:
        answer.appendleft(b)
    elif a == 2:
        answer.insert(1, b)
    else:
        answer.append(b)
print(*answer)