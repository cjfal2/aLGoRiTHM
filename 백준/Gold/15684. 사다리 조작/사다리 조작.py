def check():
    '''
    사다리를 타는 함수
    '''
    for start in range(N):
        m = start # m: 열 (세로선 위치)
        for n in range(H): # n: 행 (가로선 위치)
            if ladder[n][m]:
                # 오른쪽으로 이동하는 다리라면
                m += 1
            elif m > 0 and ladder[n][m-1]:
                # 왼쪽으로 이동하는 다리라면
                m -= 1
        if start != m: # 하나라도 제 위치가 아니면
            return 0
    return 1


def dfs(x, y, cnt):
    '''
    x: 가로선 위치 (행)
    y: 세로선 위치 (열)
    '''
    global answer

    if check():
        answer = min(answer, cnt)
        return
    
    if cnt == 3 or answer <= cnt:
        return

    # 브루트포스로 모든 가능성을 검색
    for i in range(x, H):
        # x행 부터 시작하여 H행 까지 검색
        k = 0 # 탐색 세로줄 위치 (열)
        if i == x: # 열이 변경되지 않았으므로 찾던 계속 탐색하기 위해 세로선 위치를 다시 저장
            k = y
    
        for j in range(k, N-1): # 마지막까지 가면 안되므로 N-1
            if not ladder[i][j] and not ladder[i][j+1]: # 다리가 양쪽에 놓여있지 않다면
                ladder[i][j] = 1
                # 이어진 곳을 또 이으면 안돼서 (가로선위치+2) j+2를 해준다.
                dfs(i, j+2, cnt+1)
                ladder[i][j] = 0


N, M, H = map(int, input().split())
# 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H
if not M:
    # 조건 충족
    print(0)
    quit()

# 사다리 정보
ladder = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1 # 이미 있는 가로선 (세로선을 연결)


answer = 4 # 최대 가로 선 수, (만약, 정답이 3보다 큰 값이면 -1을 출력)
dfs(0, 0, 0)
# 만약, 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.
print(answer) if answer < 4 else print(-1)
