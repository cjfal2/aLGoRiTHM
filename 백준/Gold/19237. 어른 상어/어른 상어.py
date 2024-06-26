"""
상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다.
상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.
N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다.

맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
자신의 냄새를 그 칸에 뿌린다.
냄새는 상어가 k번 이동하고 나면 사라진다.

각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
이때 가능한 칸이 여러 개일 수 있는데,
그 경우에는 특정한 우선순위를 따른다.
우선순위는 상어마다 다를 수 있고,
같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.

상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.


그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다.
하나의 상어를 나타내는 네 줄 중
첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위,
두 번째 줄은 아래를 향할 때의 우선순위,
세 번째 줄은 왼쪽을 향할 때의 우선순위,
네 번째 줄은 오른쪽을 향할 때의 우선순위이다.
각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다.
가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.
"""
direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
N, M, K = map(int, input().split())
if K == 1:
    print(-1)
    quit()

pan = [[[] for _ in range(N)] for _ in range(N)]
sharks = dict()
for n in range(N):
    temp = list(map(int, input().split()))
    for m in range(N):
        if temp[m] != 0:
            sharks[temp[m]] = (n, m)
            pan[n][m].append([temp[m], K])

sharks_direction = [0] + list(map(int, input().split()))
sharks_info = dict()

for n in range(1, M+1):
    sharks_info[n] = dict()
    for i in [1, 2, 3, 4]:
        temp = list(map(int, input().split()))
        sharks_info[n][i] = temp

# print(sharks)
# print(sharks_direction)
# print(sharks_info)
# for p in pan:
#     print(p)
out_shark = set()
for t in range(1, 1001):
    # 상어 이동
    new_pan = [[[] for _ in range(N)] for _ in range(N)]
    for num in range(1, M+1):
        if num in out_shark:
            continue
        d = sharks_direction[num]
        s_info = sharks_info[num]
        x, y = sharks[num]
        for nd in s_info[d]:
            nx, ny = x + direction[nd][0], y + direction[nd][1]
            if N > nx >= 0 and N > ny >= 0 and not pan[nx][ny]:
                # 겹칠 경우! => 큰 번호 상어 아웃
                if len(new_pan[nx][ny]) > 0:
                    out_shark.add(num)
                # 안겹칠 경우
                else:
                    sharks_direction[num] = nd
                    sharks[num] = (nx, ny)
                    new_pan[nx][ny].append([num, K])
                break  # 향이 없고 안쪽에 있는 애가 하나라도 있으면
        else:  # 자신의 향을 우선순위에 따라 찾아감
            for nd in s_info[d]:
                nx, ny = x + direction[nd][0], y + direction[nd][1]
                if N > nx >= 0 and N > ny >= 0:
                    if len(pan[nx][ny]) == 1:
                        shark_n, e = pan[nx][ny][0]
                        if shark_n == num:
                            sharks_direction[num] = nd
                            sharks[num] = (nx, ny)
                            new_pan[nx][ny].append([num, K])
                            break

    # print(f"========{t}번째 이동============")
    # print(out_shark)
    # 1 하나만 남으면 종료
    for i in range(2, M+1):
        if i not in out_shark:
            break
    else:
        print(t)
        break
    # 냄새 빼고, newpan추가하기
    for n in range(N):
        for m in range(N):
            if new_pan[n][m]:
                pan[n][m] = new_pan[n][m]
            elif pan[n][m]:
                pan[n][m][0][1] -= 1
                if pan[n][m][0][1] == 0:
                    pan[n][m] = []
    # for p in pan:
    #     print(p)


else:
    # 1000을 넘어간 경우
    print(-1)