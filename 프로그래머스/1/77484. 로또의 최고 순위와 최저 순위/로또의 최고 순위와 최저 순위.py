def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    answer = 7
    for n in lottos:
        if n in win_nums:
            answer -= 1
    return [(answer - zero) if answer != 7 or zero else 6, answer if answer != 7 else 6]