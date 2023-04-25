import sys
input = sys.stdin.readline


N, H = map(int, input().strip().split())
top = [0 for _ in range(H+1)]
bot = [0 for _ in range(H+1)]
# 장애물의 크기는 H보다 작은 양수 -> 0 제외라서 H+1
for i in range(N):
    h = int(input().strip())
    # 석순 (짝수)
    if not i % 2:
        bot[h] += 1
    # 종유석
    else:
        top[H - h + 1] += 1 # (위부터)

# 위아래 구분 누적합
for j in range(1, H+1):
    top[j] += top[j - 1]
    bot[H - j] += bot[H - j + 1]

ans, cnt = 9999999999, 0
for k in range(1, H+1):
    if top[k] + bot[k] < ans:    # 제일 작게 부수는 걸 찾는 부분
        cnt = 1
        ans = top[k] + bot[k]    # 개똥벌레가 부수는 장애물 수 
    elif top[k] + bot[k] == ans: # 제일 작은 게 많으면 수를 늘림
        cnt += 1

print(ans, cnt)
