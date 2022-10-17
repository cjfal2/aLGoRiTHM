for tc in range(1, int(input())+1):
    n = int(input())
    trees = list(map(int, input().split()))
    target = max(trees)
    day1 = 0
    day2 = 0 
    for i in range(n):
        tmp = target - trees[i]
        day1 += tmp%2
        day2 += tmp//2
    while day1 + 2 <= day2:
        day1 += 2
        day2 -= 1
    if day1 > day2:
        sum_val = 2 * day2
        sum_val += 2 * (day1-day2) -1
    else:
        sum_val = day2 * 2
    print(f'#{tc} {sum_val}')