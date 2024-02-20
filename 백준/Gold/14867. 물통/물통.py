from collections import deque

def bfs():
    fa, fb, ea, eb = map(int, input().split())
    visited = set()
    visited.add((0, 0))
    q = deque([(0, 0, 0)])

    while q:
        x, y, cnt = q.popleft()
        if x == ea and y == eb:
            return cnt

        next_states = [
            (fa, y),  # A full
            (x, fb),  # B full
            (0, y),   # A empty
            (x, 0),   # B empty
            (max(0, x - (fb - y)), min(y + x, fb)),  # A to B
            (min(x + y, fa), max(0, y - (fa - x)))   # B to A
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                q.append((*state, cnt + 1))

    return -1

print(bfs())
