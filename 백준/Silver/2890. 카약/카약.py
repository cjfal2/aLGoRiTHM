def main(n, m, pan):
    answer = [0 for _ in range(10)]
    answer_dict = {}
    for i in range(n):
        for j in range(m):
            w = pan[i][j]
            if w in "123456789":
                answer_dict[w] = j

    temp = sorted(answer_dict.items(), key=lambda x: -x[1])

    prize = 0
    now_z = 9999
    for t, z in temp:
        if now_z == z:
            answer[int(t)] = prize
        elif now_z > z:
            now_z = z
            prize += 1
            answer[int(t)] = prize

    for k in range(1, 10):
        print(answer[k])


if __name__ == "__main__":
    N, M = map(int, input().split())
    P = [input() for _ in range(N)]
    main(N, M, P)
