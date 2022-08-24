for _ in range(10):
    tc = int(input())
    Q = list(map(int,input().split()))
    i = 0 # 사이클 체크
    n = 1 # 처음 빼는 수
    while Q[-1] > 0: # 끝이 0이면 끝내기
        A = Q.pop(0)-n # 맨 앞을 팝하여 n을 빼줌
        if A < 1 :  # A가 0~음수 이면 0으로 저장
            A = 0
        Q.append(A) # 큐에 집어넣음
        i += 1 # 사이클 체크
        n += 1 # 빼는 수
        if i%5 == 0: # 5번의 한 사이클이 돌면 n을 1부터 다시 시작
            n = 1
    print(f'#{tc}',*Q) # 출력