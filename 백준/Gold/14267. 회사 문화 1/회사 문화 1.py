import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dfs(x):
    for w in G[x]: # 직원에 포함된 맞후임들을 전부 확인
        happy[w] += happy[x] # 맞선임의 내리칭찬을 흡수함
        dfs(w) # 재귀
    
N, M = map(int, input().strip().split()) # N: 직원 수, M: 칭찬의 수 (2 <= N, M <= 100000)
G = [[] for _ in range(N+1)] # 맨 앞에 0번째 패딩을 준 그래프 생성, 각 위치는 직원
member = list(map(int, input().strip().split())) # 각자의 맞선임 인풋
for idx, who in enumerate(member[1:], 2) : # 2번째 직원부터 그래프를 채워 나감, enumerate을 2부터 시작
    G[who].append(idx) # 각 직원에 들어가는 숫자는 맞후임을 뜻 함

# print(G)
happy = [0 for _ in range(N+1)] # 누적 칭찬을 저장할 리스트
for _ in range(M): # M만큼 인풋을 받으면서 전체 칭찬을 일단 저장함
    listener, amount = map(int, input().strip().split())
    happy[listener] += amount

dfs(1) # 첫 번째 직원부터 시작

print(*happy[1:])
