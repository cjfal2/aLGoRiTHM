n = int(input())  # 조사 시간
m = int(input())  # 초기 차량 수

max_cars = m  # 최대 차량 수 (초기값은 m으로 설정)
for _ in range(n):
    in_cars, out_cars = map(int, input().split())  # 입구, 출구 통과 차량 수 입력
    m += in_cars - out_cars  # 터널 내 차량 수 갱신
    max_cars = max(max_cars, m)  # 최대 차량 수 갱신

    if m < 0:  # 터널 내 차량 수가 0 미만이 되면 0 출력 후 종료
        print(0)
        break
else:
    print(max_cars)  # 터널 내 차량 수가 0 미만이 된 적 없으면 최대 차량 수 출력
