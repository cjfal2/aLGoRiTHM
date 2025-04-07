n = int(input())
s = input()

# 1. 괄호 수가 다르면 불가능
if s.count('(') != s.count(')'):
    print(-1)
else:
    total_time = 0
    balance = 0
    last_invalid_start = -1

    for i in range(n):
        if s[i] == '(':
            balance += 1
        else:
            balance -= 1

        # balance가 음수가 되면 invalid 구간 시작
        if balance < 0 and last_invalid_start == -1:
            last_invalid_start = i
        # balance가 다시 0이 되면 invalid 구간 종료
        elif balance == 0 and last_invalid_start != -1:
            total_time += i - last_invalid_start + 1
            last_invalid_start = -1

    print(total_time)
