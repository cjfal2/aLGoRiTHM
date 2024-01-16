# 퍼즐을 2차원 배열이 아닌 1차원으로 생각하기
# 그런데 이동은 또 2차원 배열
# 1234567890 의 배열로 만들기
# visited는 집합으로하여 key:value = 퍼즐모양:이동수
# 최소 이동수 출력

pan = ""
for i in range(3):
    pan += "".join(list(input().split()))

visited = {pan: 0}
q = [pan]
# bfs
while q:
    pan = q.pop(0)
    cnt = visited[pan]
    where_zero = pan.index('0')  # 0의 위치

    if pan == '123456780':
        print(cnt)
        quit()

    x = where_zero // 3  # 2차원 배열로 바꿨을 때의 행
    y = where_zero % 3   # 2차원 배열로 바꿨을 때의 열

    for dx, dy in (1, 0), (0, 1), (0, -1), (-1, 0), :
        nx, ny = x + dx, y + dy
        if 3 > nx >= 0 and 3 > ny >= 0:  # 이동 가능
            # 다시 리스트의 인덱스로 => nz 자리랑 where_zero 자리랑 바꾸고 방문 여부 확인
            nz = nx * 3 + ny
            list_pan = list(pan)
            list_pan[where_zero], list_pan[nz] = list_pan[nz], list_pan[where_zero]
            new_pan = "".join(list_pan)

            if not visited.get(new_pan):
                visited[new_pan] = cnt + 1
                q.append(new_pan)

print(-1)
