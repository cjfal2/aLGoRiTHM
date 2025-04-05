def min_cost(X, Y, S):
    n = len(S)
    dp = {'C': float('inf'), 'J': float('inf')}

    # 초기 상태
    if S[0] == '?':
        dp['C'] = 0
        dp['J'] = 0
    else:
        dp[S[0]] = 0

    for i in range(1, n):
        ndp = {'C': float('inf'), 'J': float('inf')}
        chars = ['C', 'J'] if S[i] == '?' else [S[i]]

        for curr in chars:
            if S[i-1] == '?':
                # 이전이 '?'라면 두 가지 모두 고려
                ndp[curr] = min(
                    ndp[curr],
                    dp['C'] + (X if curr == 'J' else 0),
                    dp['J'] + (Y if curr == 'C' else 0)
                )
            else:
                prev = S[i-1]
                cost = 0
                if prev + curr == 'CJ':
                    cost = X
                elif prev + curr == 'JC':
                    cost = Y
                ndp[curr] = min(ndp[curr], dp[prev] + cost)
        dp = ndp

    return min(dp.values())

# 전체 처리
T = int(input())
for t in range(1, T + 1):
    X, Y, S = input().split()
    X, Y = int(X), int(Y)
    result = min_cost(X, Y, S)
    print(f"Case #{t}: {result}")
