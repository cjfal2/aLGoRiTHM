import sys
input = sys.stdin.readline

    #Input
n,m,b = map(int,input().split())    #b: 인벤토리
case = []   #블록 input 저장
max_block = 0   #input중 max
min_block = 256 #input중 min
sum_block = 0   #input 총합
for i in range(n):  #입력받기
    lst = list(map(int,input().split()))
    if max(lst) > max_block:    #최대 층
        max_block = max(lst)
    if min(lst) < min_block:    #최소 층
        min_block = min(lst)
    sum_block += sum(lst)       #총 갯수
    case.append(lst)

ans = -1    #정답 - 시간
ans_block = False   #정답 - 층수
for blocks in range(max_block,min_block -1,-1):
    if blocks * m * n > sum_block +b:   #제작 가능성 판단
        continue    #기존 인벤토리로 해당 층으로 매끈하게 못하면 pass
    time_block = 0      #걸리는 시간 초기화
    flag = False        #true면 탐색 종료(이미 최소값보다 커질때 True로)
    for i in range(n):
        for j in range(m):
            if case[i][j] < blocks: #기준보다 낮음 >> 쌓기(1초)
                time_block += blocks - case[i][j]
                if time_block >= ans and ans != -1:
                     #이미 최소값 초과 & 최초의 데이터가 아님
                    flag = True #이미 최소값 오버로 패스 판단
                    break
            elif case[i][j] > blocks: #기준보다 높음 >> 제거(2초)
                time_block += 2 * (case[i][j] - blocks)
                if time_block >= ans and ans != -1:
                     #이미 최소값 초과 & 최초의 데이터가 아님
                    flag = True #이미 최소값 오버로 패스 판단
                    break
        if flag:    
            break

    if flag == False:  
        if ans == -1:
            ans = time_block
            ans_block = blocks
        else:
            if time_block < ans:
                ans = time_block
                ans_block = blocks

print(ans,ans_block)