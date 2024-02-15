def solution(skill, skill_trees):
    answer = 0
    info = dict()
    for i in range(len(skill)):
        info[skill[i]] = i
        

    for st in skill_trees:
        check = [False for _ in range(len(skill)+1)]
        flag = True
        for k in st:
            if k in skill:
                for idx in range(info[k]):
                    if not check[idx]:
                        flag = False
                check[info[k]] = True
        if flag:
            answer += 1
            
    return answer