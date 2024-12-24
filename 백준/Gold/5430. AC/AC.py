import sys
input = sys.stdin.readline


tc = int(input())
for _ in range(tc):
    p = input().strip()
    n = int(input().strip())
    arr_input = input().strip()
    if n == 0:
        if 'D' in p:
            print('error')
        else:
            print('[]')
        continue
    arr = list(map(int, arr_input[1:-1].split(',')))
    
    # R 명령어를 실제로 뒤집지 않고 방향만 기록
    is_reversed = False
    # 앞에서 삭제할 개수와 뒤에서 삭제할 개수를 기록
    front = 0
    back = 0
    
    for command in p:
        if command == 'R':
            is_reversed = not is_reversed
        elif command == 'D':
            if front + back >= len(arr):
                print('error')
                break
            if is_reversed:
                back += 1
            else:
                front += 1
    else:  # break 없이 루프가 끝났을 때
        if front + back > len(arr):
            print('error')
        else:
            result = arr[front:len(arr)-back]
            if is_reversed:
                result = result[::-1]
            print(f"[{','.join(map(str, result))}]")