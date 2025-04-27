import sys

T = int(sys.stdin.readline())
for t in range(1, T + 1):
    x = int(sys.stdin.readline())
    p = sys.stdin.readline().strip()

    i = 0
    n = len(p)
    res = 0

    while i < n:
        # 부호 처리
        sign = 1
        if p[i] == '+':
            i += 1
        elif p[i] == '-':
            sign = -1
            i += 1

        # 계수 읽기
        c = 0
        coef_exist = False
        while i < n and p[i].isdigit():
            c = c * 10 + int(p[i])
            i += 1
            coef_exist = True

        # X 유무 확인
        if i < n and p[i] == 'X':
            i += 1
            if not coef_exist:
                c = 1
            e = 1
            if i < n and p[i] == '^':
                i += 1
                e = 0
                while i < n and p[i].isdigit():
                    e = e * 10 + int(p[i])
                    i += 1
        else:
            e = 0

        res += sign * c * (x ** e)

    print(f"Case #{t}: {res}")
