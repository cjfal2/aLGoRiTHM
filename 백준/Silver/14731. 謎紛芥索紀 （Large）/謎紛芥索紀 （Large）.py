MOD = 10**9 + 7

def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    terms = data[1:]
    result = 0

    for i in range(N):
        C = int(terms[2 * i])
        K = int(terms[2 * i + 1])
        if K == 0:
            continue  # 상수항은 미분 시 사라짐
        power = mod_pow(2, K - 1, MOD)
        term_value = (C * K % MOD) * power % MOD
        result = (result + term_value) % MOD

    print(result)

if __name__ == "__main__":
    main()
