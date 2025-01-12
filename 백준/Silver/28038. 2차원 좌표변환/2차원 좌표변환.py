import math
import sys
input = sys.stdin.readline


for _ in range(int(input().strip())):
    coord_type = int(input().strip())  # 좌표계 번호 (1: 직교, 2: 극좌표계)
    a, b = map(float, input().strip().split())  # 좌표 입력

    if coord_type == 1:  # 직교좌표계 -> 극좌표계
        r = math.sqrt(a ** 2 + b ** 2)
        theta = math.atan2(b, a)  # atan2는 y, x를 받음
        if theta < 0:
            theta += 2 * math.pi  # 0 <= theta < 2*pi
        print(f"{r:.8f} {theta:.8f}")
    elif coord_type == 2:  # 극좌표계 -> 직교좌표계
        x = a * math.cos(b)
        y = a * math.sin(b)
        print(f"{x:.8f} {y:.8f}")
