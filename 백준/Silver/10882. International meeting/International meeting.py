def utc_parse(utc):
    return float(utc.replace("UTC", ""))


N = int(input())
time, base_utc = input().split()
base_hour, base_minute = map(int, time.split(":"))
total_minute = base_hour * 60 + base_minute
base_utc = utc_parse(base_utc)

for _ in range(N):
    input_utc = utc_parse(input())
    utc_gap = base_utc - input_utc
    minute_gap = utc_gap * 60
    cal_minute_gap = total_minute - minute_gap
    cal_hour, cal_minute = map(int, divmod(cal_minute_gap, 60))
    if cal_hour >= 24:
        cal_hour -= 24
    elif cal_hour < 0:
        cal_hour += 24
    cal_hour, cal_minute = str(cal_hour), str(cal_minute)
    if len(cal_hour) == 1:
        cal_hour = "0"+cal_hour
    
    if len(cal_minute) == 1:
        cal_minute = "0"+cal_minute

    print(f"{cal_hour}:{cal_minute}")
        
