# 숫자와 7세그먼트 코드 매핑
code_to_num = {
    "063": "0", "010": "1", "093": "2", "079": "3", "106": "4",
    "103": "5", "119": "6", "011": "7", "127": "8", "107": "9"
}
num_to_code = {v: k for k, v in code_to_num.items()}

def decode(segment_code):
    return "".join(code_to_num[segment_code[i:i+3]] for i in range(0, len(segment_code), 3))

def encode(number):
    return "".join(num_to_code[digit] for digit in str(number))

while True:
    line = input()
    if line == "BYE":
        break
    
    a_code, b_code = line.split("+")
    b_code, _ = b_code.split("=")

    a = int(decode(a_code))
    b = int(decode(b_code))
    c = a + b
    c_code = encode(c)

    print(f"{a_code}+{b_code}={c_code}")
