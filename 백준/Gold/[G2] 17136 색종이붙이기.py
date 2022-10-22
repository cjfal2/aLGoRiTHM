def fill(x1, y1, k):
    """
    x1 : x좌표
    x2 : y좌표
    k : 색종이의 한 변의 크기
    SWEA 파리퇴치 문제를 오마주
    색종이를 채울 수 있는지 확인하는 함수
    못채우면 False 채울 수 있으면 True
    """
    for x2 in range(k):
        for y2 in range(k):
            if not pan[x1+x2][y1+y2]:
                return False
    return True


def vis(a1, b1, kkan, boool):
    """
    색종이판에 해당 색종이 붙이기(원래는 visit이었으나 판을 바로 바꿔줌)
    이거또한 파리퇴치를 오마주
    boool을 주어서 붙일땐 0 , 뗄뗀 1을 줌
    여기서 total을 하나씩 빼거나 더해줘야 가지치기가 잘 들어감
    """
    global pan, total
    for a2 in range(kkan):
        for b2 in range(kkan):
            pan[a1+a2][b1+b2] = boool
            if boool == 0:
                total -= 1
            else:
                total += 1


def origami(x, y, su):
    """
    x : x 좌표 (행)
    y : y 좌표 (열)
    su : 사용한 색종이의 수
    재귀로 호출 할 함수
    """
    global co, total

    # 색종이수가 최소 색종이수를 넘어갔다면 가지치기
    if co < su:
        return
    # 전체 수가 0 인데
    if total == 0:
        # co 가 su 보다 클 경우 co에 su를 저장하여 최소값을 뽑아줌
        if co > su:
            co = su
        return

    if y >= 10: # y가 범위를 넘어가면 가지치기
        return

    if x >= 10: # x가 범위를 넘어갔다면 재귀를 (0행, 오른쪽열) 부터 다시 시작
        origami(0, y+1, su)
        return

    if pan[x][y] == 1: # 판xy가 1이라면 색종이를 붙이자
        for k in range(5, 0, -1): # 색종이를 5부터 작아지게 맞춰봄(5부터해야 시간이 빠를것 같아서)
            if base[k] and x - 1 + k < 10 and y - 1 + k < 10 and fill(x, y, k): # 색종이가 있고, 범위 안쪽이며, 붙일 수 있으면
                vis(x, y, k, 0) # 붙이기
                base[k] -= 1 # 색종이 이용
                origami(x + k, y, su + 1) # 재귀
                base[k] += 1 # 색종이 도르마무
                vis(x, y, k, 1) # 떼기

    else: # 판xy 가 1이 아니면 행만 옮겨봄
        origami(x + 1, y, su)


base = [5 for _ in range(6)] # 색종이가 5개씩 있으니까~   (0번째 색종이는 인덱싱을 위해 무시)
pan = []
total = 0 # 1의 총 수
for vv in range(10): # 뽀문 바로 돌면서 total이랑 pan을 채워줌
    a = list(map(int, input().split()))
    pan.append(a)
    total += a.count(1)

co = 9999999999 # 겁나 큰애 넣어줌

origami(0, 0, 0) # dfs 시작

if co != 9999999999: # co가 변했다면
    print(co)
else: # 안변했다면, 주어진 색종이로 표현을 못하는것이므로
    print(-1)