import sys

def power(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

def hamming_number(p1, p2, p3, i):
    result = set()  # 중복 방지

    for j in range(60):
        b = power(p1, j)
        for k in range(60):
            c = power(p2, k)
            a = b * c
            result.add(a)
            for l in range(60):
                if j + k + l >= 59:
                    break
                a *= p3
                result.add(a)

    sorted_result = sorted(result)  # 정렬 후 i번째 값 출력
    return sorted_result[i]

p1, p2, p3, i = map(int, sys.stdin.readline().split())
print(hamming_number(p1, p2, p3, i))
