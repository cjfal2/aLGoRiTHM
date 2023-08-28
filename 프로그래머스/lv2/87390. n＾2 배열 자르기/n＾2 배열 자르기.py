def solution(n, left, right):
    pan = []
    for i in range(left, right+1):
        a, b = divmod(i, n)
        if a >= b:
            pan.append(a+1)
        else:
            pan.append(b+1)
    return pan