d = {
    "MON": 6,
    "TUE": 5,
    "WED": 4,
    "THU": 3,
    "FRI": 2,
    "SAT": 1,
    "SUN": 7
}
for tc in range(int(input())):
    print(f'#{tc+1} {d.get(input())}')
