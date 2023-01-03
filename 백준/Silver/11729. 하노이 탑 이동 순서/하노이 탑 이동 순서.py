def hanoi(NUM, X, Y):
    """
    X번 기둥에서 Y번 기둥으로 옮기는 것
    기둥 번호의 합이 1+2+3=6 이라서
    시작 기둥과 목표 기둥이 어디든지
    6-X-Y는 중간 기둥의 번호임
    """
    if NUM > 1:
        hanoi(NUM-1, X, 6-X-Y)
    print(X, Y)
    if NUM > 1:
        hanoi(NUM-1, 6-X-Y, Y)

n = int(input())
print(2**n-1) # 점화식
if n <= 20:
    hanoi(n,1,3) # X