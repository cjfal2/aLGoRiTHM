def solution(s):
    ans = []
    temp = []
    temstr = ''
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for idx, i in enumerate(s[1:-1]):
        if i in nums:
            temstr += i
        elif i == ',' and s[1:-1][idx-1] != '}':
            temp.append(int(temstr))
            temstr = ''
        elif i == '}':
            temp.append(int(temstr))
            temstr = ''
            ans.append([len(temp), temp])
            temp = []
    ans.sort()
    answer = []
    for i in ans:
        for j in i[1]:
            if j not in answer:
                answer.append(j)
                break
        
    return answer