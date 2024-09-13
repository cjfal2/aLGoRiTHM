def solve(number):
    root = int(number**(1/2))
    # 제곱수인 경우 약수의 개수가 홀수
    return root * root == number

input()  # 첫 번째 input은 사용되지 않으므로 생략 가능
numbers = list(map(int, input().split()))

# 각 숫자에 대해 제곱수인지 판별하고 결과를 바로 출력
for n in numbers:
    if solve(n):
        print(1, end=" ")
    else:
        print(0, end=" ")
