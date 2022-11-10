'''
1. N,M,K 입력
2. M번 반복으로 파이어볼 정보 입력
3. 파이어볼 정보는 fireballs[]에 저장.
?? "한 점에 파이어볼 두 개 이상이 있다"라는 것을 어떻게 알까?
- arr(각 칸은 [])를 만들어 직접 파이어볼을 넣고 움직여서 브루트 포스로 length가 2이상인 arr를 뽑는다?
- fireballs를 for문 돌며 ... no


for K 로 move()
move 후 for 문으로 fireballs를 돌며 arr[(N*N)]에 각 칸에 fireball정보 append
for 끝난 후 브루트포스로 length가 2이상인 칸에서 gather()
* gather전에 same 등의 이름으로 더미데이터 True 생성,
for 문으로 2 이상의 칸 돌며 홀짝 여부가 전 것과 같다면 pass 아니라면 same을 False로 토글
if 질량합//5로 가지치고

if same:
0246으로 네 개의 파이어볼 fireballs에 append,
else:
1357으로 네 개의 파이어볼 fireballs에 append
fireballs에서 기존의 합쳐진 파이어볼들 remove
'''

def move():
    global fireballs, arr
    directions=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    for i in fireballs:
        i[0] += directions[i[4]][0]*i[3]
        i[1] += directions[i[4]][1] * i[3]
        i[0] = (i[0]) % N
        i[1] = (i[1]) % N
        arr[i[0]][i[1]].append(i)


def gather():
    global fireballs, arr
    new_fire = []
    for i in arr:
        for j in i:
            if 1 > len(j):
                continue
            elif len(j) == 1:
                new_fire.append(j[0])
            else:
                mass = 0
                speed = 0
                same = True
                for k in range(len(j)):
                    mass += j[k][2]
                    speed += j[k][3]
                    if k == 0:
                        if j[k][4] in odd:
                            standard = odd
                        else:
                            standard = even
                        row = j[k][0]
                        col = j[k][1]
                    else:
                        if j[k][4] not in standard:
                            same = False
                mass_avg = mass // 5
                if mass_avg:
                    speed_avg = speed // len(j)
                    if same:
                        new_fire.append([row, col, mass_avg, speed_avg, 0])
                        new_fire.append([row, col, mass_avg, speed_avg, 2])
                        new_fire.append([row, col, mass_avg, speed_avg, 4])
                        new_fire.append([row, col, mass_avg, speed_avg, 6])
                    else:
                        new_fire.append([row, col, mass_avg, speed_avg, 1])
                        new_fire.append([row, col, mass_avg, speed_avg, 3])
                        new_fire.append([row, col, mass_avg, speed_avg, 5])
                        new_fire.append([row, col, mass_avg, speed_avg, 7])
    return new_fire

N, M, K = map(int, input().split())
fireballs = []
arr = [[[] for __ in range(N)] for _ in range(N)]
odd = [1, 3, 5, 7]
even = [0, 2, 4, 6]
for balls in range(M):
    fireballs.append(list(map(int, input().split())))
for ball in fireballs:
    ball[0] -= 1
    ball[1] -= 1

for moves in range(K):
    move()

    fireballs = gather()

    arr = [[[] for __ in range(N)] for _ in range(N)]
ans = 0
for item in fireballs:
    ans += item[2]

print(ans)