def feb_check(feb):
    # 윤년 확인
    if feb % 4 == 0:
        if feb % 100 == 0:
            if feb % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def is_valid_date(day, month, year):
    days_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if feb_check(year):
        days_month[2] = 29
    
    if month < 1 or month > 12:
        return False
    
    if day < 1 or day > days_month[month]:
        return False
    
    return True


while True:
    d, m, y = map(int, input().split())
    
    if d == m == y == 0:
        break
    
    print("Valid" if is_valid_date(d, m, y) else "Invalid")
