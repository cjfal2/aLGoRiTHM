def cal():
    """
    bfs 함수
    return: 최소 연산값
    """
    visited = [0] * 1000001 # visited를 최대 수 만큼 생성
    visited[N] = 1 # visited가 담는 수는 연산의 수
    q = [N] # 뀨
    while q:
        t = q.pop(0) # 뀨니까 맨 앞 꺼냄
        for x in [t+1, t-1, t*2, t-10]: # 가능한 연산에 대하여 bfs 시행
            if x < 1 or M+11 < x:   # 제일 중요한 가지치기 대충 M+11 보다 크면 최소 연산이 안될 것 같아서 설정
                continue
            if not visited[x]:
                if x == M: # 해당 수일 경우 리턴, 이 때는 무조건 최소연산이 된다
                    return visited[t]
                visited[x] = visited[t] + 1 # visited가 담는 수는 연산의 수
                q.append(x) # 뀨에 *저*장*


for tc in range(int(input())):
    N, M = map(int, input().split())
    print(f'#{tc+1}', cal())
