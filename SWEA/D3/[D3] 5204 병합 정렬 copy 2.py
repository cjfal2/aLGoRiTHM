def merge_sort(m):
    """
    분할과정
    """
    global co
    if len(m) <= 1:
        return m
    # 찢는 부분
    mid = len(m)//2
    # 리스트의 크기가 1이 될 때까지 merge_sort 재귀 호출
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    """
    병합 과정
    """
    if left[-1] > right[-1]:
        co += 1

    result = [] # 두 개의 분할된 리스트를 병합하여 result를 만듦
    
    x, y = 0, 0  # 재귀 + 포인터 방식
    while len(left) > x and len(right) > y: # 양쪽 리스트에 원소가 남아있는 경우
        # 두 서브 리스트의 원소들을 비교하여 작은 것부터 result에 추가함
        if left[x] <= right[y]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[y])
            y += 1

    result += left[x:]
    result += right[y:]

    return result


for tc in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    co = 0
    res = merge_sort(L)
    print(f'#{tc+1}', res[N//2], co)