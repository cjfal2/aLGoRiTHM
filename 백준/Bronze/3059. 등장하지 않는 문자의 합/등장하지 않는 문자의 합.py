for tc in range(int(input())):
    memo = set(list(input()))
    answer = 0
    for x in "QWERTYUIOPASDFGHJKLZXCVBNM":
        if x not in memo:
            answer += ord(x)
    print(answer)