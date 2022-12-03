from collections import deque
# 큐를 이용할 것 이므로 deque를 빠르게 임포트 해준다.

def queue(t):
    '''
    t: 단계 별 i**3
    '''
    if t == 1:
        Q.popleft()
        return
        
    Q.rotate(-(t-1))
    Q.popleft()     # 탈락시키고 return을 줘서 함수를 종료한다.
    return


# 인풋을 바로 받으면서 Q(큐) 에 각 사람의 번호를 부여해준다.
Q = deque()
for i in range(1, int(input())+1):
    Q.append(i)

for i in range(1, len(Q)): # 입력의 참가자 수 만큼 순회한다.
    t = (i**3)%len(Q) # t단계 에서의 세제곱 수를 저장해준다. 세제곱수라서 연산이 오래걸리기 때문에 나머지를 이용해 시간을 줄인다.
    queue(t) # 함수 호출을 해준다.
print(Q[0])
