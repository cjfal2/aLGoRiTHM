from collections import deque

def bfs(N, K):
    visited = set()
    q = deque([(N, 0)])
    cnt = 0
    min_time = 1000000
    
    while q:
        position, now = q.popleft()
        visited.add(position)
        
        if now > min_time:  # 이미 최소 시간을 넘어간 경우
            continue
        
        if position == K:  # 동생을 찾은 경우
            if now < min_time:
                min_time = now
                cnt = 1
            elif now == min_time:
                cnt += 1
            continue
        
        next_positions = [position - 1, position + 1, position * 2]
        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                q.append((next_pos, now + 1))
    
    return min_time, cnt

N, K = map(int, input().split())
min_time, cnt = bfs(N, K)
print(min_time)
print(cnt)
