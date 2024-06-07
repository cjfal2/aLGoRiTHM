def solve(students):
    temp = [0 for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            for year in range(5):
                if students[i][year] == students[j][year]:
                    temp[i] += 1
                    temp[j] += 1
                    break

    max_count = max(temp)
    for i, cnt in enumerate(temp):
        if cnt == max_count:
            return i + 1


n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
print(solve(students))
