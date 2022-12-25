def solution(n):
    fibo = [0,1]
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        for i in range(n-1):
            fibo.append(fibo[-1] + fibo[-2])
        return fibo[-1]%1234567