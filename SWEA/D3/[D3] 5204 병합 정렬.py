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
        ans.append(left[-1])
    result = [] # 두 개의 분할된 리스트를 병합하여 result를 만듦
    while len(left) > 0 and len(right) > 0: # 양쪽 리스트에 원소가 남아있는 경우
        # 두 서브 리스트의 첫 원소들을 비교하여 작은 것부터 result에 추가함
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0: # 왼쪽 리스트에 원소가 남아있을 경우
        result.extend(left)
    if len(right) > 0: # 오른쪽 리스트에 원소가 남아있을 경우
        result.extend(right)
    return result




for tc in range(int(input())):
    N = int(input())
    L = list(map(int, input().split()))
    ans = []
    co = 0
    res = merge_sort(L)
    print(f'#{tc+1}', res[N//2], co)