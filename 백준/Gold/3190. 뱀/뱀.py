'''
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데,
사과를 먹으면 뱀 길이가 늘어난다.
뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

1.  게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다.

2. 보드의 상하좌우 끝에 벽이 있다.

3. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다.

4. 뱀은 처음에 오른쪽을 향한다.

5. 뱀은 매 초마다 이동

6. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
   만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.

7. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
   즉, 몸길이는 변하지 않는다.

Q. 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''
from collections import deque

N = int(input())
base = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(int(input())):
   a, b = map(int, input().split())
   base[a-1][b-1] = 2

info = [] # 시간, 회전
for _ in range(int(input())):
   a, b = list(input().split())
   info.append([int(a), b])
info.sort()

# for v in base:
#    print(v)
# print(info)

time = 0
dix = 0 # 0우 1하 2좌 3상
direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake = deque()
snake.append((0, 0))

x, y = 0, 0
while 1:
   time += 1
   # print(f'=========time:{time}=========')
   # print(f'dix:{dix}')
   bx, by = x, y
   x += direc[dix][0]
   y += direc[dix][1]
   if N > x >= 0 and N > y >= 0:
      if (x, y) in snake:
         print(time)
         quit()         

      if base[x][y] == 2:
         base[x][y] = 0
         snake.appendleft((x, y))
      elif base[x][y] == 0:
         snake.pop()
         snake.appendleft((x, y))

      # for aaa in base:
      #    print(aaa)
      # print(f'snake:{snake}')

      if info and info[0][0] == time:
         # print("정보에 걸림")
         n, d = info.pop(0)
         # print(n, d)
         if d == "L":
            dix -= 1
            if dix == -1:
               dix = 3
         else:
            dix += 1
            if dix == 4:
               dix = 0
   else:
      print(time)
      quit()