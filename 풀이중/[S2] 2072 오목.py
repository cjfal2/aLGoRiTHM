def omok():
    global win
    for i in range(14):
        for j in range(14):
            

pan = [[0 for _ in range(19)] for _ in range(19)]
win = False
for su in range(1, int(input())+1):
    x, y = map(int, input().split())
    x, y = x-1, y-1
