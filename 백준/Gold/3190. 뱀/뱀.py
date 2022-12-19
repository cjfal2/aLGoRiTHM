from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
base = [[0 for _ in range(N)] for _ in range(N)] # 판을 만듦

for _ in range(int(input())):
   a, b = map(int, input().split())
   base[a-1][b-1] = 2 # 인덱스 맞추기 위해 1씩 빼줘서 2를 저장 (2 = 사과)

info = [] # [시간, 회전]
for _ in range(int(input())):
   a, b = list(input().split())
   info.append([int(a), b])
info.sort() # 혹시 시간이 뒤죽박죽 올까봐 sort

time = 0 # 시간 변수
dix = 0 # 0우 1하 2좌 3상을 표시할 것임
direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]

snake = deque()
snake.append((0, 0)) # 뱀의 정보를 deque로 저장

x, y = 0, 0 # 초기 머리의 x, y 좌표
while 1:
   time += 1 # 시간 증가

   x += direc[dix][0] # 머리 x 좌표 이동
   y += direc[dix][1] # 머리 y 좌표 이동

   if N > x >= 0 and N > y >= 0: # 범위 안쪽이면
      if (x, y) in snake: # 이동한 머리가 snake deque 안에 있으면 종료
         print(time)
         quit()         

      # 머리 위치에 따른 몸 길이 증식 판단
      if base[x][y] == 2: # 머리가 사과위치라면
         base[x][y] = 0 # 사과를 없애고
         snake.appendleft((x, y)) # 맨 앞에 머리만 추가 (몸 길이 증가)
      elif base[x][y] == 0: # 아무것도 없다면
         snake.pop() # 맨 뒤를 빼고
         snake.appendleft((x, y)) # 맨 앞에 머리 추가

      # 방향전환 판단
      # infomation에 정보가 있고, 맨 앞이 현재 시간과 같을 때
      if info and info[0][0] == time:
         n, d = info.pop(0) # 맨 앞을 빼고
         if d == "L": # 왼쪽으로 틀어라
            dix -= 1
            if dix == -1:
               dix = 3
         else: # 오른쪽으로 틀어라
            dix += 1
            if dix == 4:
               dix = 0
   else:
      print(time) # 범위 밖이면 종료
      quit()