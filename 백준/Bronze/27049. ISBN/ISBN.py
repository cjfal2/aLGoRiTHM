def main(text):
    # '?' 위치 찾기
    missing_index = text.index('?')

    # 브루트포스: 0~9 또는 'X' 대입 후 유효성 검사
    for digit in range(10):
        # ISBN의 '?'를 현재 digit으로 대체
        test_isbn = text[:missing_index] + str(digit) + text[missing_index + 1:]

        # ISBN 유효성 검사
        if is_valid_isbn(test_isbn):
            return digit

    # 마지막 자리가 X일 가능성 확인
    if missing_index == 9:  # '?'가 마지막 자리에만 가능
        test_isbn = text[:missing_index] + 'X' + text[missing_index + 1:]
        if is_valid_isbn(test_isbn):
            return 'X'

    # 유효한 숫자가 없으면 -1 반환
    return -1


def is_valid_isbn(text):
    total = 0
    for i in range(10):
        if text[i] == 'X':
            value = 10  # 'X'는 10으로 간주
        else:
            value = int(text[i])
        total += value * (10 - i)

    return total % 11 == 0


if __name__ == "__main__":
    print(main(input()))



