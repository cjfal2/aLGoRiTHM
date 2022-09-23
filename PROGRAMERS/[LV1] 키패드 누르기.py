numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'


def solution(numbers, hand):
    where = {
        1  : [0, 0],
        2  : [0, 1],
        3  : [0, 2],
        4  : [1, 0],
        5  : [1, 1],
        6  : [1, 2],
        7  : [2, 0],
        8  : [2, 1],
        9  : [2, 2],
        '*': [3, 0],
        0  : [3, 1],
        '#': [3, 2]
    }

    now_R = [3, 2]
    now_L = [3, 0]
    s = []
    for num in numbers:
        if num in [3, 6, 9]:
            s.append('R')
            now_R = where.get(num)

        elif num in [1, 4, 7]:
            s.append('L')
            now_L = where.get(num)
            
        else:
            now = where.get(num)
            R = abs(now_R[0]-now[0])+abs(now_R[1]-now[1])
            L = abs(now_L[0]-now[0])+abs(now_L[1]-now[1])
            if R < L:
                s.append('R')
                now_R = where.get(num)
            elif R > L:
                s.append('L')
                now_L = where.get(num)
            elif R == L:
                if hand == 'right':
                    s.append('R')
                    now_R = where.get(num)
                else:
                    s.append('L')
                    now_L = where.get(num)

    answer = ''.join(s)
    return answer


print(solution(numbers, hand))