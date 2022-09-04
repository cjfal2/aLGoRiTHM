from collections import deque


word = list(input())
bomb = list(input())
q = deque()
for i in range(len(word)):
    q.append(word[i])
    if len(q) >= len(bomb):
        for j in range(len(bomb), 0, -1):
            if q[-j] != bomb[len(bomb)-j]:
                break
        else:
            for _ in range(len(bomb)):
                q.pop()
# q.pop()
if len(q) == 0:
    print("FRULA")
else:
    print(*q, sep="")
