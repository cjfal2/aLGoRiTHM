N = int(input())
nyaong = input()

alphabet = {
    "q": 0,
    "w": 0,
    "e": 0,
    "r": 0,
    "t": 0,
    "y": 0,
    "u": 0,
    "i": 0,
    "o": 0,
    "p": 0,
    "a": 0,
    "s": 0,
    "d": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "z": 0,
    "x": 0,
    "c": 0,
    "v": 0,
    "b": 0,
    "n": 0,
    "m": 0,
}

alphabet_count, start, end, answer = 0, 0, 0, 0
# end먼저 이동 => start 이동으로 최대길이 찾기
while end < len(nyaong):
    if alphabet[nyaong[end]] == 0:  # 등장하지 않은 알파벳이라면
        alphabet_count += 1
    alphabet[nyaong[end]] += 1  # 그 알파벳 수 올리기

    # 알파벳 수가 N을 초과했다면 start 움직일 차례
    while alphabet_count > N:
        alphabet[nyaong[start]] -= 1  # 그 알파벳 빼줌
        if alphabet[nyaong[start]] == 0:  # 0이되면 총 카운트 빼줌
            alphabet_count -= 1
        start += 1

    answer = max(answer, end - start + 1)
    end += 1  # end 이동

print(answer)
