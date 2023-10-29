import sys
sys.setrecursionlimit(100000)

# 문자열이 절대 없으면 -1, 싸이클이면 -1

def dfs(x, y, now_word_len, cnt):
    global answer

    visited[x][y] = 1
    if now_word_len % L == 0 and cnt > answer[0]: # 나누어 떨어지고(문자열이 완성)
        answer = (cnt, x+1, y+1)

    for nx, ny in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
        if N > nx >= 0 and M > ny >= 0 and pan[nx][ny] == word[now_word_len % L]:
            if visited[nx][ny] and now_word_len % L == 0: # 싸이클 생성
                print(-1)
                quit()

            if now_word_len % L: # 길이로 나누어 떨어지지지 않으면 cnt는 그대로
                dfs(nx, ny, now_word_len + 1, cnt)
            else:
                dfs(nx, ny, now_word_len + 1, cnt+1)

    visited[x][y] = 0


N, M, L = map(int, input().split())
word = input()
pan = [input() for _ in range(N)]
visited = [[0 for _ in range((M))] for _ in range(N)]
answer = (-1, -1, -1) # 처음의 answer

dfs(0, 0, 1, 1)
if answer[0] != -1:
    print(answer[0])
    print(answer[1], answer[2])
else:
    print(-1)
