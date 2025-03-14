import sys

input = sys.stdin.readline

def count_trajectories(P):
    # 에라토스테네스의 체를 이용하여 P 이하의 소수 찾기
    sieve = [True] * (P + 1)
    sieve[0] = sieve[1] = False
    primes = []

    for i in range(2, P + 1):
        if sieve[i]:
            primes.append(i)
            for j in range(i * i, P + 1, i):
                sieve[j] = False

    # DP 배열 초기화
    dp = [0] * len(primes)
    dp[0] = 1  # 항상 2는 방문해야 하므로 1로 설정

    # DP 계산
    for i in range(1, len(primes)):
        for j in range(i - 1, -1, -1):
            if primes[i] - primes[j] > 14:
                break  # 14를 초과하면 중단
            dp[i] += dp[j]

    return dp[-1]  # 마지막 소수를 방문하는 모든 경우의 수

# 입력
P = int(input().strip())

# 출력
print(count_trajectories(P))
