answer = set()
def dfs(arr, v, t):
    global answer
    a = sum(arr)
    if a == t and sum(v) != 0:
        answer.add(tuple(arr))
        return

    for i in range(len(arr)):
        if not v[i]:
            arr[i] *= -1
            v[i] = 1
            dfs(arr, v, t)
            v[i] = 0
            arr[i] *= -1
        else:
            return
def solution(numbers, target):
    visited = [0 for _ in range(len(numbers))]
    dfs(numbers, visited, target)
    return len(answer)