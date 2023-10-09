N = int(input())
arr = []
for i in range(1, N+1):
    a, b = map(int, input().split())
    # 끝나는 날이 퇴사일 넘어가는거 빼주기
    if i+a-1 < N+1:
        arr.append([i, i+a-1, b]) # [시작하는 날, 끝나는 날, 일당]
if arr:
    M = len(arr) # arr의 최종 길이
    dp = [0 for _ in range(M+1)] # dp 배열에 각 날짜에 받을 수 있는 최대 수당을 넣어줄 것임
    dp[0] = arr[0][2] # 첫째날 값 넣어주기

    for i in range(1, M):
        cost = arr[i][2]  # 현재 시작일의 수당
        
        # 이전 까지 근무일 까지 비교
        for j in range(i):
            # 이전 끝나는 날이랑 지금 시작날이랑 겹치지 않는 경우
            if arr[j][1] < arr[i][0]: 
                # 현재 값 vs 안 겹치는 구간의 최대 값에 현재 값을 더한 것 중 최대값
                cost = max(cost, dp[j] + arr[i][2])
        # dp에 저장
        dp[i] = cost

    # dp에서 최대값
    print(max(dp))
else:
    print(0)