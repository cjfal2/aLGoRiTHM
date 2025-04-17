import math
import sys

def cad_to_usd(cad, rate):
    return math.floor(cad / rate * 0.97 * 100) / 100

def usd_to_cad(usd, rate):
    return math.floor(usd * rate * 0.97 * 100) / 100

def solve():
    input = sys.stdin.read
    lines = input().strip().splitlines()
    
    idx = 0
    while idx < len(lines):
        if lines[idx] == '0':
            break

        d = int(lines[idx])
        idx += 1

        rates = []
        for _ in range(d):
            rates.append(float(lines[idx]))
            idx += 1

        cad = 1000.0
        usd = 0.0

        for i in range(d):
            rate = rates[i]
            
            # 이전 값을 저장
            prev_cad = cad
            prev_usd = usd

            # 가능한 선택지: 둘 중 큰 값 선택
            # (1) CAD 유지 or USD → CAD
            cad = max(prev_cad, usd_to_cad(prev_usd, rate))
            # (2) USD 유지 or CAD → USD
            usd = max(prev_usd, cad_to_usd(prev_cad, rate))

        # 마지막 날은 무조건 CAD로 계산
        print(f"{cad:.2f}")

solve()
