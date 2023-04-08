MAX = 10000

def change(num, i, j):
    if i == 0 and j == 0:
        return -1
    m = 1
    for k in range(3 - i):
        m *= 10
    a = num % m
    b = num // (m * 10)
    b *= (m * 10)
    return a + b + m * j

def bfs(start, end):
    primes = [True] * (MAX + 1)
    for i in range(2, int(MAX**0.5) + 1):
        if primes[i]:
            for j in range(2*i, MAX + 1, i):
                primes[j] = False
    
    dist = [0] * (MAX + 1)
    visited = [False] * (MAX + 1)
    q = []
    q.append(start)
    visited[start] = True
    while q:
        num = q.pop(0)
        for i in range(4):
            for j in range(10):
                next_num = change(num, i, j)
                if next_num != -1:
                    if primes[next_num] and not visited[next_num]:
                        q.append(next_num)
                        visited[next_num] = True
                        dist[next_num] = dist[num] + 1
    return dist[end]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))
