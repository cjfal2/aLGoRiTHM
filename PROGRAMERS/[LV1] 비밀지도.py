# n = 6
# arr1 = [46, 33, 33 ,22, 31, 50]
# arr2 = [27, 56, 19, 14, 14, 10]
#

def solution(n, arr1, arr2):
    def tobin(arr3):
        bin1 = []
        for i in arr3:
            a = str(bin(i))[2:]
            while len(a) != n:
                if len(a) < n:
                    a = '0' + a
            bin1.append(a)
        return bin1
    b1 = tobin(arr1)
    b2 = tobin(arr2)

    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if b1[i][j] == "1" or b2[i][j] == "1":
                temp += "#"
            elif b1[i][j] == "0" and b2[i][j] == "0":
                temp += " "
        answer.append(temp)

    return answer
# print(solution(n, arr1, arr2))