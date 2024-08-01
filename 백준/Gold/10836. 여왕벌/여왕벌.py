M, N = map(int, input().split())
hive = [[1 for _ in range(M)] for _ in range(M)]
for _ in range(N):
    growth_record = [[0 for _ in range(M)] for _ in range(M)] # 성장도 기록

    # 인풋
    zero, one, two = map(int, input().split())
    # 자라는 정도를 리스트로 구현
    growth = [0 for _ in range(zero)] + [1 for _ in range(one)] + [2 for _ in range(two)]
    
    # 가장자리의 성장 (왼쪽 밑 시작 => 위 => 오른쪽)
    x, y = M-1, 0 # 시작 지점을 왼쪽 밑으로 설정한다.
    
    # growth의 인덱스를 맞춰준다.
    for grow_idx in range(2*M-1): # 루프문을 통해서 점을 이동시키며 성장시킨다. 2M -1 만큼 이동하면 종료
        growth_amount = growth[grow_idx]
        hive[x][y] += growth_amount # 성장 정도 만큼 성장시킨다.
        growth_record[x][y] += growth_amount # 성장도를 기록한다.

        # x값이나 y값 중 하나를 옮긴다.
        if x == 0:
            y += 1
        else:
            x -= 1
    
    # (1, 1) 부터 (M-1, M-1) 까지 순회하면서 성장도와 hive에 기록
    for x in range(1, M):
        for y in range(1, M):
            # 왼, 왼위, 위의 성장도 확인하여 가장 큰 값을 체크
            how_here_growth = max(growth_record[x][y-1], growth_record[x-1][y-1], growth_record[x-1][y])
            growth_record[x][y] = how_here_growth # 성장도 저장
            hive[x][y] += how_here_growth # 벌집에 성장도 반영
for h in hive:
    print(*h)