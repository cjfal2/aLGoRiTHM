import math
import functools

# 입력
n = int(input())

# 0이 아닌 모든 자리수 추출 및 LCM 계산
digits = {int(d) for d in str(n) if d != '0'}  # set을 사용하여 중복 제거
k = functools.reduce(math.lcm, digits)  # 여러 개의 숫자에 대해 LCM 계산

# n이 k의 배수라면 그대로 출력
if n % k == 0:
    print(n)
else:
    cnt = 1
    while True:
        for i in range(10**cnt):
            candidate = int(f"{n}{i:0{cnt}d}")  # 앞에 0을 채워서 숫자 생성
            if candidate % k == 0:
                print(candidate)
                exit()  # 가장 먼저 찾은 결과 출력 후 종료
        cnt += 1
