def function_one(cmd):
    _, arr_idx = cmd
    arr_idx -= 1
    temp = pan[arr_idx][:]
    temp.insert(0, temp.pop())

    pan[arr_idx] = temp[:]


def function_two():
    global pan

    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1] = pan[i][j]
    pan = temp[:]


def print_pan():
    for p in pan:
        print(*p)


N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
for _ in range(int(input())):
    command = list(map(int, input().split()))
    if len(command) == 1:
        function_two()
    else:
        function_one(command)
print_pan()