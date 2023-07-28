def solution(priorities, location):
    new = [i for i in range(len(priorities))]
    cnt = 0
    while 1:

        x = priorities.pop(0)
        y = new.pop(0)
        
        flag = True
        for p in priorities:
            if p > x:
                flag = False
                break
        if flag:
            cnt += 1
            if y == location:
                return cnt
        else:
            priorities.append(x)
            new.append(y)
