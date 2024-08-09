def three_times(num):
    return num ** 3


def solve(num):
    return num * (num + 1) * (num + 2) // 6


while 1:
    num = int(input())
    if not num:
        break

    answer = 0

    i = 1
    while three_times(i) <= num:
        answer = max(answer, three_times(i))
        i += 1

    j = 1
    while solve(j) <= num:
        answer = max(answer, solve(j))
        j += 1

    i = 1
    while three_times(i) <= num:
        j = 1
        while solve(j) <= num:
            temp = three_times(i) + solve(j)
            if temp <= num:
                answer = max(answer, temp)
            j += 1
        i += 1

    print(answer)
