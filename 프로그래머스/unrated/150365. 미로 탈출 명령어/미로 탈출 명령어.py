from collections import deque


def solution(n, m, x, y, r, c, k):
    if abs(x - r) + abs(y - c) < 0:
        return "impossible"

    q = deque([(x, y, "", 0)])
    while q:
        i, j, p, cnt = q.popleft()
        if i == r and j == c and (k - cnt) % 2: # 도착을 했는데 홀수만큼 남았다면
            return "impossible"
        if i == r and j == c and cnt == k: # 도착을 했는데 딱 떨어졌다면
            return p
        for di, dj, dix in (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u'):
            ni, nj = i + di, j + dj
            if n >= ni > 0 and m >= nj > 0 and abs(ni - r) + abs(nj - c) + cnt + 1 <= k:
                q.append((ni, nj, p + dix, cnt + 1))
                break

    return "impossible"