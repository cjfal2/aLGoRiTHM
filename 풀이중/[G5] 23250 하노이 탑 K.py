from collections import deque

def hanoi(NUM, X, Y):
    if NUM > 1:
        hanoi(NUM-1, X, 6-X-Y)
    L.append((X, Y))
    if len(L) == k:
        print(L.pop())
        quit()
    if NUM > 1:
        hanoi(NUM-1, 6-X-Y, Y)

n, k = map(int, input().split())
L = deque()
hanoi(n,1,3) # X