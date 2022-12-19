s = "one4seveneight"


def solution(s):
    trans = {
        'zero' : '0',
        'one'  : '1',
        'two'  : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six'  : '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9'
    }
    for alpha, num in trans.items():
        s = s.replace(alpha, num)
    answer = s
    return answer


print(solution(s))