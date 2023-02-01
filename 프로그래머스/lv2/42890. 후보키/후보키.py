
def solution(relation):

    def dfs(start):
        if s and tuple(s) not in temp:
            temp.append(tuple(s))
        for i in range(start, N):
            if not visited[i]:
                visited[i] = 1
                s.append(i)
                dfs(i)
                s.pop()
                visited[i] = 0 

    answer = []
    N = len(relation[0])
    M = len(relation)
    s = []
    visited = [0 for _ in range(N)]
    temp = []
    
    dfs(0)

    for comb in sorted(temp, key= lambda x: len(x)):
        temp1 = []
        for rel in relation:
            temp2 = []
            for com in comb:
                temp2.append(rel[com])  
            temp1.append(tuple(temp2))
        # 유일성
        if len(set(temp1)) == M:
            flag = True

             # 최소성
            for ans in answer:
                # 집합의 소집합(?) 인지 판단하여 소집합이면 컷
                if set(ans).issubset(set(comb)):
                    flag = False
                    break
                    
            if flag:
                answer.append(comb)
   
    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","comflager","3"],["400","con","comflager","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))
print(solution([["a","1","aaa","c","ng"],["a","1","bbb","e","g"],["c","1","aaa","d","ng"],["d","2","bbb","d","ng"]]))