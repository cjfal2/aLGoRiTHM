S = int(input())
q = [(1, 0, 0)]  # 화면, 클립보드, 시간
visited = set()  # 방문
visited.add((1, 0, 0))
while q:
    screen, clip_board, time = q.pop(0)
    if screen == S:
        print(time)
        break
    for s, c, t in (screen, screen, time+1), (screen+clip_board, clip_board, time+1), (screen-1, clip_board, time+1):
        if (s, c, t) not in visited:
            visited.add((s, c, t))
            q.append((s, c, t))