import sys
input = sys.stdin.readline

N, M = map(int, input().split())

package_price = []
single_price = []

for _ in range(M):
    package, single = map(int, input().split())
    package_price.append(package)
    single_price.append(single)

min_package = min(package_price)
min_single = min(single_price)

# 1. 패키지로만 사는 경우
cost1 = (N // 6) * min_package + (min_package if N % 6 != 0 else 0)
# 2. 낱개로만 사는 경우
cost2 = N * min_single
# 3. 패키지 + 낱개로 사는 경우
cost3 = (N // 6) * min_package + (N % 6) * min_single

print(min(cost1, cost2, cost3))
