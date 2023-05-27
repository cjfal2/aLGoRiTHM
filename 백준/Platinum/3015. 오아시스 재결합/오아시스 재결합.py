import sys
input = sys.stdin.readline


s = []
ans = 0
for _ in range(int(input())):
    h = int(input())
    while s and s[-1][0] < h: # s가 없거나 마지막 스택의 높이가 작으면
        ans += s[-1][1]
        s.pop()

    # 맨 앞에 사람
    if not s:
        s.append((h, 1))
    else:
        # 같은 키
        if s[-1][0] == h:
            now_h, now_cnt = s.pop()
            ans += now_cnt
            # 제일 큰 사람과 쌍
            if s:
                ans += 1

            # 연속해서 같은 키
            now_cnt += 1
            s.append((now_h, now_cnt))

        # 더 작은 사람
        else:
            s.append((h, 1))
            # 제일 큰 사람과 쌍
            ans += 1

print(ans)
