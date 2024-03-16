import datetime
a = {
    0: "MON",
    1: "TUE",
    2: "WED",
    3: "THU",
    4: "FRI",
    5: "SAT",
    6: "SUN",
}
m, d = map(int, input().split())
print(a[datetime.datetime(year=2007, month=m, day=d).weekday()])