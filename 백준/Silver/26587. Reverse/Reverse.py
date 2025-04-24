import sys

def is_vowel(word):
    return word and word[0].lower() in {'a','e','i','o','u'}

for line in sys.stdin:
    line = line.strip()
    if not line:
        print()
        continue

    words = line.split(' ')
    # 모음 단어 위치와 단어 수집
    vow_pos = []
    vow_words = []
    for i, w in enumerate(words):
        if is_vowel(w):
            vow_pos.append(i)
            vow_words.append(w)
    # 모음 단어들만 뒤집기
    vow_words.reverse()
    # 뒤집힌 단어를 원위치에 덮어쓰기
    for idx, pos in enumerate(vow_pos):
        words[pos] = vow_words[idx]
    # 결과 출력
    print(' '.join(words))
