def main(N, arr):
    results = [0]
    min_value = arr[0]  # 첫 번째 값이 최솟값 초기값
    max_difference = 0
    for i in range(1, N):
        temp_max_difference = arr[i] - min_value
        if temp_max_difference > max_difference:
            max_difference = temp_max_difference
        results.append(max_difference)
        min_value = min(min_value, arr[i])

    return " ".join(map(str, results))



if __name__ == "__main__":
    print(main(int(input()), list(map(int, input().split()))))