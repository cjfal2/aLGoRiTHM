for tc in range(int(input())):
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))

    A = [1, 2, 3, 3, 4, 10]
    B = [1, 2, 2, 2, 3, 5, 10]
    
    a, b = 0, 0
    for i in range(6):
        a += (n[i] * A[i])
        b += (m[i] * B[i])

    b += (m[-1] * B[-1])

    answer = ''
    if a > b:
        answer = "Good triumphs over Evil"
    elif a == b:
        answer = "No victor on this battle field"
    else:
        answer = "Evil eradicates all trace of Good"
    print(f'Battle {tc+1}: {answer}')
        