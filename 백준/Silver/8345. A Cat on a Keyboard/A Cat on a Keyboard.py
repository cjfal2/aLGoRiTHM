# 키보드 행 정의 (이미지 기준)
row1 = "`1234567890-="
row2 = "qwertyuiopQWERTYUIOP[]\\"
row3 = "asdfghjklASDFGHJKL;'"
row4 = "zxcvbnmZXCVBNM,./"
row5 = " "  # 스페이스바

# 입력 받기
text = input()

# 변환된 문자열 생성
result = []
for char in text:
    if char in row1:
        result.append("1")
    elif char in row2:
        result.append("2")
    elif char in row3:
        result.append("3")
    elif char in row4:
        result.append("4")
    elif char in row5:
        result.append("5")

# 출력
print("".join(result))
