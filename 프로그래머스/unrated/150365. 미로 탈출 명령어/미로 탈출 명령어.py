from collections import deque


def solution(n, m, x, y, r, c, k):
    check = abs(x - r) + abs(y - c) # 거리체크
    if check > k or check % 2 != k % 2:  # 거리가 k보다 멀거나 남은 거리랑 이동수가 다르면
        return "impossible"

    q = deque([(x, y, "", 0)]) # 좌표x 좌표y 경로 이동수
    while q:
        i, j, p, cnt = q.popleft()
        if i == r and j == c and (k - cnt) % 2:  # 도착을 했는데 홀수만큼 남았다면
            return "impossible"
        if i == r and j == c and cnt == k:  # 도착을 했는데 딱 떨어졌다면
            return p
        for di, dj, dix in (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u'): # 사전순이 빠른순으로 길을 찾아야하니까 dlru순서로
            ni, nj = i + di, j + dj
            if n >= ni > 0 and m >= nj > 0 and abs(ni - r) + abs(nj - c) < k - cnt: # 범위 안쪽이고 갈 수 있으면
                q.append((ni, nj, p + dix, cnt + 1))
                break

    return "impossible"