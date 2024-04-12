R, C, K = map(int, input().split())
directions = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, 1),
    4: (0, -1)
}
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.

pan = dict()
for _ in range(K):
    r, c, s, d, z = map(int, input().split())
    r -= 1
    c -= 1
    pan[(r, c)] = [s, d, z]


getted_shark = 0
for m_fisher in range(C):
    # 2. 상어 잡기
    for n_fisher in range(R):
        shark = pan.get((n_fisher, m_fisher))
        if shark:
            getted_shark += shark[2]
            pan.pop((n_fisher, m_fisher))
            break  # 반드시 멈춰줘야함

    new_pan = dict()
    # 3. 상어 이동
    for n in range(R):
        for m in range(C):
            if pan.get((n, m)):
                s, d, size = pan[(n, m)]
                speed = s
                nx, ny = n, m
                if d in [1, 2]:
                    c = R * 2 - 2
                    if d == 1:
                        speed += 2 * (R - 1) - n
                    else:
                        speed += n

                    speed %= c
                    if speed >= R:
                        nx, d = 2 * R - 2 - speed, 1
                    else:
                        nx, d = speed, 2

                else:
                    c = C * 2 - 2
                    if d == 4:
                        speed += 2 * (C - 1) - m
                    else:
                        speed += m

                    speed %= c
                    if speed >= C:
                        ny, d = 2 * C - 2 - speed, 4
                    else:
                        ny, d = speed, 3

                if (nx, ny) not in new_pan or new_pan[(nx, ny)][2] < size:
                    new_pan[(nx, ny)] = [s, d, size]
    pan = new_pan

print(getted_shark)
