def back(obs_num):
    if obs_num == 3:
        # 선생의 시야 계산
        if watch():
            print("YES")
            quit()
        return

    for i in range(N):
        for j in range(N):
            if pan[i][j] == "X":
                pan[i][j] = "O"
                back(obs_num+1)
                pan[i][j] = "X"


def watch():
    discover = 0
    for x, y in teachers:
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x, y
            while 1:
                nx += dx
                ny += dy
                if discover:
                    break

                if N <= nx or 0 > nx or N <= ny or 0 > ny:
                    break

                if pan[nx][ny] == "O":
                    break

                if pan[nx][ny] == "S":
                    discover += 1

    if discover:
        return False
    return True


N = int(input())
pan = []
teachers = set()
students = set()
stu_num = 0
for n in range(N):
    a = input().split()
    for m in range(N):
        if a[m] == "T":
            teachers.add((n, m))
        elif a[m] == "S":
            students.add((n, m))
            stu_num += 1
    pan.append(a)

back(0)
print("NO")
