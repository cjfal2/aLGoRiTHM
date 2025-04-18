def solve_rebus(line):
    parts = line.split()
    result = ""

    for part in parts:
        # 왼쪽에서 연속된 ' 개수
        left = 0
        while left < len(part) and part[left] == "'":
            left += 1
        
        # 오른쪽에서 연속된 ' 개수
        right = 0
        while right < len(part) and part[len(part) - 1 - right] == "'":
            right += 1

        # 실제 단어 추출
        word = part[left:len(part) - right if right != 0 else None]
        trimmed = word[left:len(word) - right if right != 0 else None]
        result += trimmed

    return result

# 입력 및 출력 처리
line = input().strip()
print(solve_rebus(line))
