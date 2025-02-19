import sys

# 7-segment 숫자 패턴 사전
DIGIT_PATTERNS = {
    (".XX.", "X..X", "X..X", "....", "X..X", "X..X", ".XX."): "0",
    ("....", "...X", "...X", "....", "...X", "...X", "...."): "1",
    (".XX.", "...X", "...X", ".XX.", "X...", "X...", ".XX."): "2",
    (".XX.", "...X", "...X", ".XX.", "...X", "...X", ".XX."): "3",
    ("....", "X..X", "X..X", ".XX.", "...X", "...X", "...."): "4",
    (".XX.", "X...", "X...", ".XX.", "...X", "...X", ".XX."): "5",
    (".XX.", "X...", "X...", ".XX.", "X..X", "X..X", ".XX."): "6",
    (".XX.", "...X", "...X", "....", "...X", "...X", "...."): "7",
    (".XX.", "X..X", "X..X", ".XX.", "X..X", "X..X", ".XX."): "8",
    (".XX.", "X..X", "X..X", ".XX.", "...X", "...X", ".XX."): "9"
}

def parse_digit(segment, start_col):
    """ 7줄의 ASCII 아트에서 숫자 하나를 파싱하여 반환 """
    digit_segment = tuple(row[start_col:start_col+4] for row in segment)
    return DIGIT_PATTERNS.get(digit_segment, "?")  # 없는 패턴이면 "?" 반환

def read_time_from_ascii(ascii_art):
    """ 7x21 크기의 ASCII 아트에서 HH:MM 형태의 시간을 읽음 """
    digits = [
        parse_digit(ascii_art, 0),   # HH 첫 번째 자리
        parse_digit(ascii_art, 5),   # HH 두 번째 자리
        parse_digit(ascii_art, 12),  # MM 첫 번째 자리
        parse_digit(ascii_art, 17)   # MM 두 번째 자리
    ]
    return f"{digits[0]}{digits[1]}:{digits[2]}{digits[3]}"

def main():
    # 입력 처리
    T = int(sys.stdin.readline().strip())
    results = []
    
    for _ in range(T):
        ascii_art = [sys.stdin.readline().strip() for _ in range(7)]
        results.append(read_time_from_ascii(ascii_art))
    
    # 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
