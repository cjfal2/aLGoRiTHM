def main(bulbs):
    bulbs = list(bulbs)   # 문자열을 리스트로 변환
    n = len(bulbs)
    turn = 0

    for i in range(1, n + 1):
        # 현재 전구가 켜져 있으면
        if bulbs[i - 1] == 'Y':
            turn += 1
            for j in range(i, n + 1, i):
                # 반전
                bulbs[j - 1] = 'N' if bulbs[j - 1] == 'Y' else 'Y'
    return turn if all(bulb == 'N' for bulb in bulbs) else -1


if __name__ == '__main__':
    print(main(input()))
