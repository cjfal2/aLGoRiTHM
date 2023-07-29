def solution(n, words):
    answer = [0, 0]
    memo = set()
    
    last = ""
    for i, x in enumerate(words):
        
        if i == 0:
            memo.add(x)
            last = x[-1]
        else:
            if last == x[0]:
                if x in memo:
                    answer = [i%n+1, i//n+1]
                    break
                else:
                    memo.add(x)
                    last = x[-1]
            else:
                answer = [i%n+1, i//n+1]
                break
    return answer