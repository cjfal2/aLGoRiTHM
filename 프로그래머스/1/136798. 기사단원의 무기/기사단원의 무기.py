def solution(number, limit, power):
    total_iron = 0
    for i in range(1, number + 1):
        divisor_count = 0
        for j in range(1, int(i ** 0.5) + 1):  # 제곱근까지만 반복하여 약수 개수 계산
            if i % j == 0:
                if i // j == j:  # 제곱수인 경우 중복으로 카운트되므로 하나만 추가
                    divisor_count += 1
                else:
                    divisor_count += 2
        if divisor_count > limit:
            total_iron += power
        else:
            total_iron += divisor_count
    return total_iron