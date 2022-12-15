from datetime import *
for tc in range(int(input())):
    L = list(input().split())
    day1 = datetime(2022, int(L[0]), int(L[1]))
    day2 = datetime(2022, int(L[2]), int(L[3]))
    print(f'#{tc+1} {int(str(day2-day1)[:3])+1}')
