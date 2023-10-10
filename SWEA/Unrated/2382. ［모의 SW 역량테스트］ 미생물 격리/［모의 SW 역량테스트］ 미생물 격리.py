# (상: 1, 하: 2, 좌: 3, 우: 4)
direction = {
	1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1),
}

reverse = {
	1:2,
    2:1,
    3:4,
    4:3
}

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split()) # 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
    pan = dict()
    for _ in range(K):
        s, g, n, d = map(int, input().split()) # 세로위치, 가로위치, 미생물 수, 이동방향
        pan[(s, g)] = (n, d) # (s, g) 칸에 있는 미생물
    
    # 격리 시작
    for _ in range(M):
        new_pan = dict()
        for k, v in pan.items():
            numbers = v[0]
            d = v[1]
            dx, dy = direction.get(d)
            nx, ny = k[0] + dx, k[1] + dy
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                d = reverse[d]
                numbers //= 2
                
            if numbers == 0:
                continue
                
            if (nx, ny) in new_pan:
                new_pan[(nx, ny)].append((numbers, d))
            else:
                new_pan[(nx, ny)] = [(numbers, d)]
        
        pan = dict()
        for k, v in new_pan.items():
            numbers = 0
            max_num = 0
            direc = 0
            for n, d in v:
                numbers += n
                if max_num < n:
                    max_num = n
                    direc = d
            pan[k] = (numbers, direc)
    answer = 0
    for k, v in pan.items():
        answer += v[0]
    print(f'#{tc} {answer}')
            