dartResult = '1S2D*3T'


def solution(dartResult):
    arr = list(dartResult)
    s = []
    answer1 = 0
    answer2 = 0
    sang = []
    temp = 0
    idx = 0
    while arr:
        s.append(arr.pop(0))
        if s[-1] in '1234567890':
            if s[-1] == '1' and arr[0] == '0':
                s[-1] = '10'
                arr.pop(0)
                if idx == 1:
                    answer1 += temp
                elif idx == 2:
                    answer2 += temp
                temp = 0
            else:
                if idx == 1:
                    answer1 += temp
                elif idx == 2:
                    answer2 += temp
                temp = 0

        if s[-1] == 'S':
            idx += 1
            temp += int(s[-2])
        elif s[-1] == 'D':
            idx += 1
            temp += int(s[-2])**2
        elif s[-1] == 'T':
            idx += 1
            temp += int(s[-2])**3

        if s[-1] in '*#':
            sang.append([idx, s[-1]])

    answer3 = temp

    ANS = [answer1, answer2, answer3]

    if sang:
        for a, b in sang:
            a -= 1
            if b == '#':
                ANS[a] *= -1
            if b == '*':
                if a == 0:
                    ANS[0] *= 2
                else:
                    ANS[a-1] *= 2
                    ANS[a] *= 2
    answer = sum(ANS)
    return answer

print(solution(dartResult))
