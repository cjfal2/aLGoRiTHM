import sys

# 입력 받기
sentence = sys.stdin.readline().strip()

# 기본 분할: 띄어쓰기와 하이픈
words = sentence.replace('-', ' ').split()

# 줄임말 규칙에 맞는 접두어 리스트
contractions = ['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu']

# 모음 리스트 (h 포함)
vowels = set('aeiouh')

# 단어 개수 세기
count = 0
for word in words:
    # 어포스트로피가 있는 경우
    if "'" in word:
        prefix, suffix = word.split("'", 1)
        if prefix in contractions and suffix and suffix[0] in vowels:
            # 줄임말 규칙에 맞으면 분리된 두 단어로 계산
            count += 2
        else:
            # 규칙에 맞지 않으면 하나의 단어로 계산
            count += 1
    else:
        # 어포스트로피가 없는 경우 하나의 단어로 계산
        count += 1

# 결과 출력
print(count)
