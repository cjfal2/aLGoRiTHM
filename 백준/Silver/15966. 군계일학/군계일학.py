N = int(input())
memo = [0 for _ in range(10 ** 6 + 1)]
numbers = [0] + list(map(int, input().split()))
for i in range(1, N + 1):
    num = numbers[i]
    memo[num] = max(memo[num], memo[num - 1] + 1)
print(max(memo))
