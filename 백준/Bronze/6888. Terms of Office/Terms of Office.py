X = int(input())
Y = int(input())

for year in range(X, Y + 1):
    if (year - X) % 60 == 0:
        print(f"All positions change in year {year}")
