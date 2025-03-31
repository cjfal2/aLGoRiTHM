import sys
input = sys.stdin.read

def calc_win_prob(contestants, T):
    prob = 1.0
    for a, b in contestants:
        if T <= a:
            continue
        elif T >= b:
            return 0.0
        else:
            p = (T - a) / (b - a)
            prob *= (1 - p)
            if prob < 0.5:
                break  # 이미 확률이 0.5보다 작으면 더 계산할 필요 없음
    return prob

def solve():
    data = input().split()
    n = int(data[0])
    contestants = [(float(data[i]), float(data[i+1])) for i in range(1, len(data), 2)]

    lo = 0.0
    hi = 100000.0
    eps = 1e-7

    while hi - lo > eps:
        mid = (lo + hi) / 2
        if calc_win_prob(contestants, mid) >= 0.5:
            lo = mid
        else:
            hi = mid

    print(f"{lo:.15f}")

solve()
