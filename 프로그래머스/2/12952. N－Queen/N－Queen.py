ans = 0
def solution(n):
    def queen(start):
        global ans
        
        if start == n:
            ans += 1
            return
        for i in range(n):
            if not check_hang[i] and not check_degak_1[start+i] and not check_degak_2[start-i+(n-1)]:
                pan[start] = i
                check_hang[i] = check_degak_1[start+i] = check_degak_2[start-i+(n-1)] = 1
                queen(start+1)
                check_hang[i] = check_degak_1[start+i] = check_degak_2[start-i+(n-1)] = 0

    pan = [0] * n
    check_hang = [0] * n    # ㅡ
    check_degak_1 = [0] * ((n*2)-1)   # /
    check_degak_2 = [0] * ((n*2)-1)   # \

    queen(0)

    return ans