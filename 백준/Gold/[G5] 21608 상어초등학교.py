import sys
input = sys.stdin.readline


def find(p, arr):
    """
    base를 채우는 함수
    빈칸을 찾고 그 빈칸에서 4방향을 확인
    확인하는 것: 좋아하는 친구가 몇명인지, 빈칸이 몇개인지

    베이스 xy에 뭐 숫자가 있으면 옆 4방향 탐색??
    """
    inform = [] # 빈칸들의 정보
    for x in range(N):
        for y in range(N):
            if base[x][y] == 0: # 빈칸이라면
                temp = 0 # 주위 빈칸의 수
                like = 0 # 주위 좋아하는 애 수
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]: # 델타 탐색
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and N > ny >= 0: # 범위 내에서
                        if not base[nx][ny]: # 그 빈칸의 상/하/좌/우 가 빈칸이면
                            temp -= 1 # 빈칸수를 음수로 세줌 (정렬을 위해)
                        else:
                            if base[nx][ny] in arr:
                                like -= 1 # 좋아수를 음수로 세줌 (정렬을 위해) 
                inform.append([like, temp, x, y]) # 정보에 넣어줌

    inform.sort(key=lambda x: (x[0], x[1], x[2], x[3])) # 람다를 이용해서 중요한 순서로 정렬을 해줌
    xx, yy = inform[0][2], inform[0][3] # 맨앞에 있는 x좌표, y좌표를 저장
    base[xx][yy] = p # base를 해당 숫자로 바꿔줌


N = int(input().strip())

base = [[0 for _ in range(N)] for _ in range(N)] # 기반이 될 이중 리스트
base_dic = dict() # 정보를 담아서 마지막에 만족도를 얻기위해 사용

for k in range(N**2): # N의 2제곱 만큼 인풋이 들어옴
    t, *L = map(int, input().strip().split()) # 인풋을 숫자, 좋아하는애들(리스트)로 받아줌
    base_dic[t] = L # 베이스딕셔너리에 저장   {4: [2,5,1,7]}
    if k == 0:
        base[1][1] = t # 처음엔 무조건 1, 1 자리에 저장됨
    else: # 처음이 아니라면
        find(t, L)

ans = 0 # 만족도를 담을 변수
for x in range(N):
    for y in range(N):
        likes = base_dic.get(base[x][y]) # 내가 좋아하는 애들 정보 불러오기
        love = 0 # 좋아하는 애 수
        for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nx, ny = x + dx, y + dy
            if N > nx >= 0 and N > ny >= 0:
                if base[nx][ny] in likes: # 좋아하는 애들 정보에 있으면
                    love += 1
        """
        이제 학생의 만족도를 구해야 한다.
        학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다.
        학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다.
        그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
        """
        if love == 1:
            ans += 1
        elif love == 2:
            ans += 10
        elif love == 3:
            ans += 100
        elif love == 4:
            ans += 1000
print(ans)