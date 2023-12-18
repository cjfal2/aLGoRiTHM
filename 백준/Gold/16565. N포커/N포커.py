def comb(N, K):
    if cards[N][K]:
        return cards[N][K]

    if K == 0 or K == N:
        cards[N][K] = 1
    else:
        cards[N][K] = (comb(N - 1, K - 1) + comb(N - 1, K)) % mod

    return cards[N][K]


N = int(input())
cards = [[0 for _ in range(53)] for _ in range(53)]
mod = 10007
answer = 0

for i in range(1, N//4 + 1):
    if i % 2:
        answer += (comb(13, i) * comb(52 - i*4, N - i*4)) % mod
        answer %= mod
    else:
        answer -= (comb(13, i) * comb(52 - i*4, N - i*4)) % mod
        answer = (answer + mod) % mod

print(answer)
