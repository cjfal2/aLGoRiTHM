N = int(input())  # 소의 수
cows = []  # 소들
for _ in range(N):
    position, speed = map(int, input().split())
    cows.append((position, speed))

# 마지막 그룹의 속도를 마지막 그룹 첫 번째 소의 속도로 지정
last_speed = cows[-1][1]
groups = 1  # 최소 한 개의 그룹은 존재

# 뒤에서부터 확인
for i in range(N - 2, -1, -1):
    if cows[i][1] > last_speed:  # 마지막 그룹의 속도보다 빠르다면
        # 이 소는 앞의 소를 따라잡을 것이므로 같은 그룹에 속해야 함
        continue
    else:
        # 빠르지 않다면 새로운 그룹이 만들어짐
        last_speed = cows[i][1]
        groups += 1

print(groups)
