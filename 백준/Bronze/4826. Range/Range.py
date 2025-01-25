def calculate_range():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    results = []
    i = 0

    while i < len(data):
        instance = []
        
        while i < len(data):
            line = data[i].strip()
            i += 1

            # 입력을 (odometer, fuel)로 변환
            try:
                odometer, fuel = map(float, line.split())
            except ValueError:
                continue

            if (odometer, fuel) == (0.0, 0.0):
                break
            if (odometer, fuel) == (-1.0, -1.0):
                return results

            instance.append((odometer, fuel))
        
        # 유효한 데이터가 있는 경우 처리
        if len(instance) >= 2:
            total_distance = 0.0
            total_fuel_used = 0.0

            for j in range(1, len(instance)):
                prev_odometer, prev_fuel = instance[j - 1]
                cur_odometer, cur_fuel = instance[j]

                # 연료가 감소한 경우만 계산
                if cur_fuel < prev_fuel:
                    total_distance += cur_odometer - prev_odometer
                    total_fuel_used += prev_fuel - cur_fuel

            # 주행 가능 거리 계산
            if total_fuel_used > 0:
                last_fuel = instance[-1][1]
                fuel_efficiency = total_distance / total_fuel_used
                estimated_range = round(last_fuel * fuel_efficiency)
                results.append(estimated_range)
    
    return results


# 결과 출력
if __name__ == "__main__":
    results = calculate_range()
    for result in results:
        print(result)
