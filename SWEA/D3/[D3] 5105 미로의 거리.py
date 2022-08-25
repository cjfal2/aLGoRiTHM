def start(arr):
    '''
    시작점을 찾는 함수
    x : 행 좌표
    y : 열 좌표
    return : x,y
    '''
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                return x,y

def bfs(i,j,N):
    '''
    너비 우선 탐색 함수
    i : 시작점 x좌표
    j : 시작점 y좌표
    N : 미로 변의 크기
    return : 거리-2 or 0(불가능)
    '''
    visited = [[0]*N for _ in range(N)] # 방문 리스트 생성
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while q: # q가 있으면
        i,j=q.pop(0) # 꺼냄
        if maze[i][j] == 3:
            return visited[i][j]-2 #3과2사이에있는 0의 수가 필요하므로 visited의 시작이 1부터 시작하기에 도착점에는 0의수+2가 된다.
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 사방을 확인해서 갈 수 있는 지점인지 확인
            ni,nj = i+di, j+dj # 사방향 다 진행하며
            # 미로의 안쪽이며 벽이아니고 방문한 지점이 아니면
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni,nj)) # 큐에 넣고
                visited[ni][nj] = visited[i][j]+1 # 방문리스트에서 그 자리의 수를 1 늘린다.
    return 0

for tc in range(int(input())):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)] # 잘라서 넣기
    for i in maze:
        print(i)
    stx,sty = start(maze)

    print(f'#{tc+1} {bfs(stx,sty,N)}')