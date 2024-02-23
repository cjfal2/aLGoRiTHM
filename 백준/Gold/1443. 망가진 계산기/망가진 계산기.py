
def cal(cnt, total, before):
    global answer

    if total > limit:
        return

    if cnt == P:
        if total > answer:
            answer = total
        return

    for num in range(max(2, before), 10):
        if total * num < limit:
            cal(cnt + 1, total * num, num)


D, P = map(int, input().split())
answer = 2 ** P
limit = 10 ** D - 1
if answer > limit:
    print("-1")
    quit()

cal(0, 1, 1)
print(answer)
