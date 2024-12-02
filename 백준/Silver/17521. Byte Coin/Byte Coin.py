n, w = map(int, input().split())
prices = [int(input()) for _ in range(n)]

cash = w
coins = 0

for i in range(n):
    # 마지막 날이면 모든 코인을 현금으로
    if i == n - 1:
        cash += coins * prices[i]
        coins = 0

    # 다음 날의 가격이 오늘보다 크다면 코인을 삼
    elif prices[i] < prices[i + 1]:
        # 살 수 있는 최대 코인
        coins += cash // prices[i]
        cash %= prices[i]
    # 다음 날의 가격이 오늘보다 작다면 코인을 팜
    elif prices[i] > prices[i + 1]:
        cash += coins * prices[i]
        coins = 0

print(cash)

