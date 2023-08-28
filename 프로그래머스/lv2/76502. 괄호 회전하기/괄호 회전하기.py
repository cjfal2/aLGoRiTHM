def solution(s):
    s = list(s)
    
    answer = 0
    N = len(s)
    
    temp ={
        "}":"{",
        ")":"(",
        "]":"["
    }
    
    def check(arr):
        stack = []
        for a in arr:
            if not stack:
                if a in "({[":
                    stack.append(a)
                else:
                    stack = [1]
                    break
            elif a in "})]":
                if stack[-1] == temp.get(a):
                    stack.pop()
                else:
                    stack = [2]
                    break
            else:
                stack.append(a)
                
        return False if stack else True
    
    for _ in range(N):
        if check(s):
            answer += 1
        s.append(s.pop(0))
    
    return answer