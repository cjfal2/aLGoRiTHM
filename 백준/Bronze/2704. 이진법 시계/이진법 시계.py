def main(time):
    h, m, s = time.split(':')
    h = list(bin(int(h)))
    m = list(bin(int(m)))
    s = list(bin(int(s)))
    h[1] = "0"
    m[1] = "0"
    s[1] = "0"
    time = [h, m, s]
    for i in range(3):
        while len(time[i]) != 6:
            if len(time[i]) < 6:
                time[i].insert(0, "0")
            else:
                time[i].pop(0)
    answer1 = ""
    for i in range(6):
        for j in range(3):
            answer1 += time[j][i]

    answer2 = ""
    for i in range(3):
        for j in range(6):
            answer2 += time[i][j]

    return [answer1, answer2]


if __name__ == "__main__":
    for _ in range(int(input())):
        print(*main(input()))