def solution(arr, k):
    if k % 2:
        return list(map(lambda x: x * k, arr))
    return list(map(lambda x: x + k, arr))