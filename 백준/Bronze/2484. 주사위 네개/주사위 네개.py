def calculate_prize(dice):
    dice.sort()
    counts = {}
    for d in dice:
        counts[d] = counts.get(d, 0) + 1

    if len(counts) == 1:  # 같은 눈 4개
        return 50000 + dice[0] * 5000
    elif len(counts) == 2:
        if 3 in counts.values():  # 같은 눈 3개
            return 10000 + list(counts.keys())[list(counts.values()).index(3)] * 1000
        else:  # 두 쌍
            return 2000 + sum(k * 500 for k in counts)
    elif len(counts) == 3:  # 같은 눈 2개
        return 1000 + list(counts.keys())[list(counts.values()).index(2)] * 100
    else:  # 모두 다른 눈
        return dice[-1] * 100

N = int(input())
max_prize = 0

for _ in range(N):
    dice = list(map(int, input().split()))
    prize = calculate_prize(dice)
    max_prize = max(max_prize, prize)

print(max_prize)
