for tc in range(int(input())):
    N,M = map(int,input().split())
    flag = [[i for i in input()] for _ in range(N)] # 붙어있는 인풋을 짤라서 리스트에 하나씩 넣어줌

    MIN = N*M # 최대 칠해야하는 경우의 수를 일단 가장 작다고 가정
    for b in range(1,N-1): # b 시작점
        for t in range(1,N-b): # b 가능 두께
            co = 0 # 바꿔야하는 색의 수
            # 각 색에 대하여 범위의 행에 대한 바꿔야하는 수를 모두 계산한다.
            #---하얀색 계산---#
            for white in range(0,b): # 0~b 처음 부터 b시작까지
                co += (M-flag[white].count('W'))
            #---파란색 계산---#
            for blue in range(b,b+t): # b~b+t b의 가능한 두께
                co += (M-flag[blue].count('B'))
            #---빨간색 계산---#
            for red in range(b+t,N): # b+t b두께 끝에서 끝까지
                co += (M-flag[red].count('R'))
            #---최소값 비교---#
            if co<MIN: # 가장 작다고 가정한 것 보다 더 작은 색칠의 경우의 수면 저장
                MIN=co

    print(f'#{tc+1} {MIN}')