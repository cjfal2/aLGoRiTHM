import sys
input = sys.stdin.readline


N = int(input())
team_time = [0, 0]  # 각 팀의 이긴 시간을 저장
score = [0, 0]      # 각 팀의 점수를 저장
last_time = 0       # 마지막으로 처리한 시간
times = []          # 모든 득점 시간과 팀 정보를 저장

# 모든 득점 정보를 수집
for _ in range(N):
    team, time = input().split()
    team = int(team) - 1  # 0, 1로 인덱싱하기 위해 1을 뺌
    min, sec = map(int, time.split(":"))
    time_in_seconds = min * 60 + sec
    times.append((time_in_seconds, team))

# 시간순으로 정렬
times.sort()

# 각 득점 시간마다 승리 시간 계산
for i, (curr_time, team) in enumerate(times):
    # 이전 시간부터 현재 시간까지 이기고 있던 팀의 시간 추가
    if score[0] > score[1]:  # 1번 팀이 이기고 있을 때
        team_time[0] += curr_time - last_time
    elif score[1] > score[0]:  # 2번 팀이 이기고 있을 때
        team_time[1] += curr_time - last_time
    
    score[team] += 1  # 현재 팀 점수 증가
    last_time = curr_time

# 마지막 득점 이후 경기 종료(48분)까지의 시간 처리
final_time = 48 * 60
if score[0] > score[1]:
    team_time[0] += final_time - last_time
elif score[1] > score[0]:
    team_time[1] += final_time - last_time

# 결과 출력 (MM:SS 형식)
for t in team_time:
    minutes = t // 60
    seconds = t % 60
    print(f"{minutes:02d}:{seconds:02d}")