for _ in range(int(input())):
    n, a, b, s1, s2 = map(int, input().split())

    pass1 = list(map(int, input().split()))
    dribble1 = list(map(int, input().split()))
    pass2 = list(map(int, input().split()))
    dribble2 = list(map(int, input().split()))

    dp1 = [float('inf')] * n
    dp2 = [float('inf')] * n

    dp1[0] = a
    dp2[0] = b

    for i in range(1, n):
        dp1[i] = min(dp1[i], dp1[i-1] + dribble1[i-1], dp2[i-1] + pass2[i-1])
        dp2[i] = min(dp2[i], dp2[i-1] + dribble2[i-1], dp1[i-1] + pass1[i-1])

    print(min(dp1[-1] + s1, dp2[-1] + s2))
