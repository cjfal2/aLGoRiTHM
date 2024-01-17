def is_palindrome_or_pseudo_palindrome(word):
    def is_palindrome(s):
        return s == s[::-1]

    left, right = 0, len(word) - 1

    while left < right:
        if word[left] != word[right]:
            # 한 문자를 삭제하여 회문이 되는지 확인
            removed_left = word[:left] + word[left + 1:]
            removed_right = word[:right] + word[right + 1:]
            if is_palindrome(removed_left) or is_palindrome(removed_right):
                return 1  # 유사회문
            else:
                return 2  # 일반 문자열
        left += 1
        right -= 1

    return 0  # 회문

# 입력 처리
T = int(input())
for _ in range(T):
    word = input().strip()
    result = is_palindrome_or_pseudo_palindrome(word)
    print(result)
