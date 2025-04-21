n, m = map(int, input().split())
times = [list(map(int, input().split())) for _ in range(n)]

bottles = [0] * m

# 각 구간에 대해 따로 처리
for j in range(m):
    events = []
    for i in range(n):
        # runner i의 구간 j 입장/퇴장 시간 계산
        enter = sum(times[i][:j])
        leave = enter + times[i][j]
        # 입장 시 +1, 퇴장 시 -1
        events.append((enter + 0.1, 1))  # 0.1: i km 진입 이후
        events.append((leave - 0.1, -1)) # leave 전까지 있음

    # 이벤트 시간 기준 정렬
    events.sort()
    curr = 0
    max_runners = 0
    for t, v in events:
        curr += v
        max_runners = max(max_runners, curr)
    
    bottles[j] = max_runners

print(' '.join(map(str, bottles)))
