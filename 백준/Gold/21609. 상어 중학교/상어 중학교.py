def gravity():
    # 검은색을 제외한 블록들이 (0 + 자연수) 다른 블록을 만나거나 벽에 닿을 때까지 떨어진다.
    for m in range(N):  # 바닥에 떨어진 부분(붙은 부분은 넘어감)부터 열 기준으로 중력 작용
        for n in range(N-2, -1, -1):
            if pan[n][m] >= 0:  # 해당 칸이 블록인 경우
                x = n
                # 다 떨어질 때 까지 중력 작용
                while 1:
                    # 아래가 블록일 경우 또는 바닥인 경우 중지
                    if x == N-1 or pan[x+1][m] >= -1:
                        break

                    # 중력 작용
                    pan[x+1][m] = pan[x][m]
                    pan[x][m] = -2
                    x += 1


def turn():
    new_pan = []
    # 판을 반시계방향으로 90도 돌린다.
    for m in range(N-1, -1, -1):
        temp = []
        for n in range(N):
            temp.append(pan[n][m])
        new_pan.append(temp)

    return new_pan


def find_group():
    '''
    일반블록은 적어도 1개 이상이고 그 일반블록들은 색이 모두 같아야 한다.
    무지개 블록을 포함해도 된다.
    검은색 블록은 절대 X
    합쳐서 2개 이상이고 붙어있어야한다.

    - 수가 제일 많은 그룹 중에서
        1: 무지개수가 많은 그룹
        2: 기준 블록의 행이 큰 그룹
        3: 기준 블록의 열이 큰 그룹
        이 기준으로 선택

    * 블록 그룹이 존재하지 않으면 게임 종료 후 점수 출력
    '''
    group = []

    visited = [[-1 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if pan[n][m] >= 1:
                block = pan[n][m]
                visited[n][m] = block
                q = [(n, m)]
                memo = (n, m)
                temp = [(n, m)]
                rainbow = 0
                while q:
                    x, y = q.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        nx, ny = x + dx, y + dy
                        if N > nx >= 0 and N > ny >= 0 and visited[nx][ny] != block:
                            if pan[nx][ny] == block:
                                visited[nx][ny] = block
                                q.append((nx, ny))
                                temp.append((nx, ny))

                            if pan[nx][ny] == 0:  # 일반 블록과 무지개 블록을 일단 함께 처리
                                visited[nx][ny] = block
                                q.append((nx, ny))
                                rainbow += 1
                                temp.append((nx, ny))

                # 블록 그룹이 안된다면
                if len(temp) < 2:
                    continue

                # 블록 그룹 선정하기
                if not group:
                    group = [len(temp), rainbow, n, m, temp]
                else:
                    if group[0] < len(temp):
                        group = [len(temp), rainbow, n, m, temp]
                    elif group[0] == len(temp):
                        if group[1] < rainbow:
                            group = [len(temp), rainbow, n, m, temp]
                        elif group[1] == rainbow:
                            if group[2] < n:
                                group = [len(temp), rainbow, n, m, temp]
                            elif group[2] == n:
                                if group[3] < m:
                                    group = [len(temp), rainbow, n, m, temp]

    return delete_group(group[4]) if group else -1  # 블록그룹이 존재하지 않으면 종료


def delete_group(g):
    # 찾은 그룹 제거, 제거된 칸은 -2로 표시
    # 칸 수의 제곱을 점수로 획득 => return
    score = 0
    for x, y in g:
        pan[x][y] = -2
        score += 1

    return score * score


N, M = map(int, input().split())  # N: 격자 크기, M: 색상의 수
pan = [list(map(int, input().split())) for _ in range(N)]

# 블록그룹이 존재하지 않으면 종료
answer = 0
while 1:
    cost = find_group()
    if cost == -1:
        break
    else:
        answer += cost
    gravity()
    pan = turn()
    gravity()

print(answer)
