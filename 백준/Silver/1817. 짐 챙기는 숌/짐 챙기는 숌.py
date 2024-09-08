N, M = map(int, input().split())

now_box = 0
answer = 0

arr = list(map(int, input().split())) if N else []

for book in arr:
    new_box = now_box + book
    if new_box <= M:
        now_box = new_box
    else:
        now_box = book
        answer += 1
if now_box:
    answer += 1
print(answer)