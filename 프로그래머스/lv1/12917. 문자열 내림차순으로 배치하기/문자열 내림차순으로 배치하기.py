def solution(s):
    arr = list(s)
    arr.sort()
    ans = ''.join(arr[::-1])
    return ans