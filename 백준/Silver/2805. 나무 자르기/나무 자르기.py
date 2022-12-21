def check(tong):
    cnt = 0 # 통나무 길이 합
    for i in L: # 배열을 순회하면서
        if i >= tong: # 통나무 길이이상이면
            cnt += i - tong # 얻을 수 있는 통나무 길이를 더함
    return cnt >= M # 원하는 길이보다 큰 지 확인

N, M = map(int, input().split())
L = list(map(int, input().split()))

start = 0 # 시작 수는 0
end = max(L) # 가장 큰 수를 끝으로

while start <= end: # 시작이 끝을 넘으면 종료
    mid = (start+end)//2 # 중간 값 저장
    if check(mid): # check가 True이면
        start = mid + 1 # 시작을 옮겨봄
    else: # check가 False면
        end = mid - 1 # 끝을 옮겨봄

print(end) # 끝이 제일 큰 거니까 출력