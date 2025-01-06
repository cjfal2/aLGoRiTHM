arr = [int(input()) for _ in range(4)]

if arr[0] == arr[1] == arr[2] == arr[3]:  # 모든 값이 동일한 경우
    print("Fish At Constant Depth")
elif arr[0] < arr[1] < arr[2] < arr[3]:  # 값이 strictly 증가하는 경우
    print("Fish Rising")
elif arr[0] > arr[1] > arr[2] > arr[3]:  # 값이 strictly 감소하는 경우
    print("Fish Diving")
else:  # 그 외의 경우
    print("No Fish")