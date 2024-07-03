# 입력 받기
yb, mb, db = map(int, input().split())
cy, cm, cd = map(int, input().split())

# 만 나이 계산
man = cy - yb - ((cm, cd) < (mb, db))

# 세는 나이 계산
se = cy - yb + 1

# 연 나이 계산
yeon = cy - yb

# 출력
print(man)
print(se)
print(yeon)
