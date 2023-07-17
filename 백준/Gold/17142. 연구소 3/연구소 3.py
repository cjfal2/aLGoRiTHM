from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline


def visit(N):
    """
    visited 생성 함수
    바이러스의 조합을 순회할 때마다 visited를 초기화해야 하므로 함수 지정
    :param N: 연구소의 크기
    :return: 벽이 체크된 visited
    """
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    # 시작점을 0부터 하여 추가 계산이 필요없게 하기위해 -1로 지정
    where_wall = list()
    for s in range(N):
        for g in range(N):
            # 벽인 경우에 체크를 해줘야 하기 때문에 -2로 벽을 세워줌
            # 벽을 체크 안하면 can에서 불가능한 경우가 되기 때문에
            if lab[s][g] == 1:
                where_wall.append([s, g])
    for s, g in where_wall:
        visited[s][g] = -2
    return visited


def can(visited):
    """
    bfs 탐색 후에 가능 여부를 체크하는 함수
    :param visited: visited 리스트
    :return: T or F
    """
    for k in visited:  # 한줄씩 봄
        if -1 in k:  # 0이 하나라도 있을 경우는 불가능한 경우이므로 바로 리턴으로 탈출
            return False
    return True


def bfs(start_list, N):
    sec = 0
    visited = visit(N)
    q = deque()
    for i, j in start_list:
        q.append([i, j])
        visited[i][j] = 0
    while q:
        s, g = q.popleft()
        for ds, dg in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ns = s + ds
            ng = g + dg
            # 빈칸이면 초를 계산한다.
            # max를 사용하는 이유: BFS의 지점마다 시간이 달라서 가장 오래걸린 시간을 계속 저장.
            if N > ns >= 0 and N > ng >= 0 and visited[ns][ng] == -1 and lab[ns][ng] == 0:
                q.append([ns, ng])
                visited[ns][ng] = visited[s][g] + 1
                sec = max(visited[ns][ng], sec)
            # 비활성 바이러스면 깨우기만 하고 시간은 세지 않는다.
            elif N > ns >= 0 and N > ng >= 0 and visited[ns][ng] == -1 and lab[ns][ng] == 2:
                q.append([ns, ng])
                visited[ns][ng] = visited[s][g] + 1
    return visited, sec


N, M = map(int, input().strip().split())
lab = [list(map(int, input().strip().split())) for _ in range(N)]
total = N * N
# 바이러스 좌표를 알아내기
covid = list()
for s in range(N):
    for g in range(N):
        if lab[s][g] == 2:
            covid.append([s, g])
            total -= 1
        if lab[s][g] == 1:
            total -= 1

if total == 0:
    print(0)
    quit()

MIN = 100000
for cov in list(combinations(covid, M)):  # 바이러스 조합으로 BFS 순회시작
    visited, sec = bfs(cov, N)
    if can(visited):
        MIN = min(sec, MIN)

if MIN == 100000:  # 갈 수 없는 경우만 있는 케이스의 경우는 MIN에 아무것도 저장 되지 않음
    print(-1)
else:
    # min(MIN)을 if문 밖으로 빼면 MIN이 빈 리스트일 때 밸류에러가남
    print(MIN)
