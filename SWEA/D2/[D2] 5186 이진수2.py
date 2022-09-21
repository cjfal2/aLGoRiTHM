"""
3
0.625
0.1
0.125

#1 101
#2 overflow
#3 001
https://ourcalc.com/2%EC%A7%84%EC%88%98-%EB%B3%80%ED%99%98%EA%B8%B0/
"""
for tc in range(int(input())):
    sosu = input()
    # 10 -> 2
    ans = ''
    for _ in range(14):
        sosu = str(float(sosu) * 2)
        # print(sosu)
        ans += sosu[0]
        sosu = '0' + str(float(sosu))[1:]
        if float(sosu) == 0:
            break

    if len(ans) >= 13:
        print(f"#{tc+1} overflow")
    else:
        print(f"#{tc+1} {ans}")