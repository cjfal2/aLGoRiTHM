N, M = map(int, input().split())
pan = [input() for _ in range(N)]

dx = [1, -1, 0,  0]  # 남, 북, 동, 서
dy = [0,  0, 1, -1]

memo = set()
answer = 0
for n in range(1, N-1):
    for m in range(1, M-1):
        if pan[n][m] == ".":
            for d in (0, 2):
                if pan[n + dx[d]][m + dy[d]] == ".":
                    if d == 0:
                        for x in range(2, 4):
                            if (
                                (n + dx[x] + dx[d], m + dy[x] + dy[d], x) not in memo and
                                pan[n + dx[x] + dx[d]][m + dy[x] + dy[d]] == "X" and
                                (n + dx[x], m + dy[x], x) not in memo and
                                pan[n + dx[x]][m + dy[x]] == "X"
                            ):
                                memo.add((n + dx[x] + dx[d], m + dy[x] + dy[d], x))
                                memo.add((n + dx[x], m + dy[x], x))
                                answer += 1
                    else:
                        for y in range(2):
                            if ((n + dx[y] + dx[d], m + dy[y] + dy[d], y) not in memo and
                                pan[n + dx[y] + dx[d]][m + dy[y] + dy[d]] == "X" and
                                (n + dx[y], m + dy[y], y) not in memo and
                                pan[n + dx[y]][m + dy[y]] == "X"
                            ):
                                memo.add((n + dx[y] + dx[d], m + dy[y] + dy[d], y))
                                memo.add((n + dx[y], m + dy[y], y))
                                answer += 1

print(answer)

