# 윤년 확인 함수
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# 각 달의 일수를 계산 (윤년 여부에 따라 2월은 다르게 처리)
def days_in_month(year, month):
    if month == 2:  # 2월 처리
        return 29 if is_leap_year(year) else 28
    # 1월, 3월, 5월, 7월, 8월, 10월, 12월은 31일, 그 외는 30일
    return 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30

# 두 날짜 간의 차이를 계산하는 함수
def calculate_days(start, end):
    start_year, start_month, start_day = start
    end_year, end_month, end_day = end

    # 천년 이상의 차이가 나는 경우 "gg" 출력
    if end_year - start_year > 1000 or (end_year - start_year == 1000 and (end_month > start_month or (end_month == start_month and end_day >= start_day))):
        return "gg"

    # 날짜 차이 계산
    days = 0

    # 연도가 다를 경우, 연도별로 일수를 더함
    while (start_year, start_month, start_day) != (end_year, end_month, end_day):
        days += 1
        start_day += 1

        # 해당 달의 마지막 날을 넘기면 다음 달로 넘어감
        if start_day > days_in_month(start_year, start_month):
            start_day = 1
            start_month += 1

        # 12월을 넘기면 다음 해로 넘어감
        if start_month > 12:
            start_month = 1
            start_year += 1

    return f"D-{days}"

# 입력 받기
start_date = tuple(map(int, input().split()))  # 시작 날짜
end_date = tuple(map(int, input().split()))    # 종료 날짜

# 결과 출력
print(calculate_days(start_date, end_date))
