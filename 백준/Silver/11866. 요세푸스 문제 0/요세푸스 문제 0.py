from collections import deque

N , K = map(int,input().split())
Q = deque()
for i in range(1, N + 1):
    Q.append(i)

L = []
i = 0
while len(L) < N:
    i += 1
    if not i%K:
        L.append(Q.popleft())
    else :
        Q.append(Q.popleft())
print('<',end='')
print(*L,sep=', ',end='')
print('>')