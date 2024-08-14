for _ in range(int(input())):
    plus, bar = divmod(int(input()), 5)
    answer = "++++ "*plus
    answer += ("|"*bar)
    print(answer)
