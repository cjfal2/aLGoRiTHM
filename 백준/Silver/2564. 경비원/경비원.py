garo, sero = map(int, input().split())
N = int(input()) # 상점의 수
stores = [list(map(int, input().split())) for _ in range(N)] # 상점 정보
dong = list(map(int, input().split())) # 동근이 위치

cost = 0
for news, distance in stores:
    if dong[0] == 1: # 북
        if news == 1:
            cost += abs(distance - dong[1])
        elif news == 2:
            what_is_min = min(sero+dong[1]+distance, sero+2*garo-dong[1]-distance)
            cost += what_is_min
        elif news == 3:
            cost += distance + dong[1]
        elif news == 4:
            cost += distance + garo - dong[1]
    elif dong[0] == 2: # 남
        if news == 1:
            what_is_min = min(sero+dong[1]+distance, sero+2*garo-dong[1]-distance)
            cost += what_is_min
        elif news == 2:
            cost += abs(distance - dong[1])
        elif news == 3:
            cost += sero - distance + dong[1]
        elif news == 4:
            cost += garo + sero - distance - dong[1]
    elif dong[0] == 3: # 서
        if news == 1:
            cost += dong[1] + distance
        elif news == 2:
            cost += sero - dong[1] + distance
        elif news == 3:
            cost += abs(distance - dong[1])
        elif news == 4:
            what_is_min = min(garo+dong[1]+distance, garo+2*sero-dong[1]-distance)
            cost += what_is_min
    elif dong[0] == 4: # 동
        if news == 1:
            cost += dong[1] + garo - distance
        elif news == 2:
            cost += sero - dong[1] + garo - distance
        elif news == 3:
            what_is_min = min(garo+dong[1]+distance, garo+2*sero-dong[1]-distance)
            cost += what_is_min
        elif news == 4:
            cost += abs(distance - dong[1])
print(cost)