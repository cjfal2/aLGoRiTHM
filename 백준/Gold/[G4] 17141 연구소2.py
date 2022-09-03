from collections import deque
from itertools import combinations
import sys


# bfs함수(시작점이 동시에 여러개인 경우)
def bfs(start_list, t):
    visited = visit(t)
    q = deque()
    for s, g in start_list:
        q.append((s, g))
        visited[s][g] = 1
    while q:
        s1, g1 = q.popleft()
        for ds1, dg1 in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ns1, ng1 = s1 + ds1, g1 + dg1
            if t > ns1 >= 0 and t > ng1 >= 0 and visited[ns1][ng1] == 0 and lab[ns1][ng1] != 1:
                q.append((ns1, ng1))
                visited[ns1][ng1] = visited[s1][g1] + 1
    return visited


# visit 생성 함수, 바이러스의 조합을 순회할 때마다 visited를 초기화해야 하므로 함수 지정
def visit(N):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    where_1 = list()
    for k in range(N):
        for u in range(N):
            if lab[k][u] == 1:  # 벽인 경우에 체크를 해줘야 하기 때문에 음수인 -1로 벽을 세워줌
                where_1.append([k, u])
    for m, n in where_1:
        visited[m][n] = -1
    return visited


# bfs 탐색 후에 그 경우에서 걸리는 최대 시간을 체크하는 함수
def mincovid(vis):
    co = 0
    for k in vis:
        if 0 in k:  # 0이 있을 경우는 불가능한 경우이므로 리턴을 말도 안되게 크게 줘서 체크
            return 100000
        else:
            if co < max(k):
                co = max(k)
    return co



input = sys.stdin.readline
N, M = map(int, input().strip().split())
lab = [list(map(int, input().strip().split())) for _ in range(N)]

# 바이러스 좌표를 알아내기
covid = list()
for s in range(N):
    for g in range(N):
        if lab[s][g] == 2:
            covid.append([s, g])
# 바이러스 좌표의 조합 구하기 (콤비네이션 임포트이용했는데 쉬프트연산자로도 가능)
if len(covid) != 1:
    covid_m = list(combinations(covid, M))
else:
    covid_m = list(covid[:])

# 알아낸 바이러스 조합으로 BFS 순회시작
MIN = [] # 순회 후 그 경우에서의  가장 긴 거리를 담을 함수
for cov in covid_m:
    MIN.append(mincovid(bfs(cov, N)))
ans = min(MIN)-1 # 1부터 시작하므로 거리는 1을 빼줌
if ans > 9999: # 갈 수 없는 경우만 있는 케이스의 경우는 100000만 MIN에 있으므로
    print(-1)
else:
    print(ans)
