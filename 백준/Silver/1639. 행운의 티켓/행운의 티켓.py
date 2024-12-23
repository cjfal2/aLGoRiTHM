numbers = input()
length = len(numbers)
answer = 0

# 가능한 모든 짝수 길이의 부분 문자열을 확인
for size in range(2, length + 1, 2):  # 짝수 길이만 확인
    for start in range(length - size + 1):
        substr = numbers[start:start + size]
        half = len(substr) // 2
        
        # 왼쪽 절반의 합과 오른쪽 절반의 합을 비교
        left_sum = sum(int(x) for x in substr[:half])
        right_sum = sum(int(x) for x in substr[half:])
        
        if left_sum == right_sum:
            answer = max(answer, size)

print(answer)
