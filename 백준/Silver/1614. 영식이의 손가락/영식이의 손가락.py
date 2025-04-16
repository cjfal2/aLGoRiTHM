def count_max_numbers(hurt_finger, max_use):
    cycle = [1, 2, 3, 4, 5, 4, 3, 2]
    length = len(cycle)

    # 손가락별 등장 인덱스 파악
    hurt_indices = [i for i, f in enumerate(cycle) if f == hurt_finger]
    use_per_cycle = len(hurt_indices)

    if max_use == 0 and cycle[0] == hurt_finger:
        return 0  # 시작조차 못함

    # 최대 몇 개의 full cycle 돌 수 있는지 계산
    full_cycles = max_use // use_per_cycle if use_per_cycle > 0 else 10**9
    used = full_cycles * use_per_cycle
    count = full_cycles * length

    # 남은 횟수로 앞에서부터 한 칸씩 늘려보기
    for i in range(length):
        finger = cycle[i]
        if finger == hurt_finger:
            if used >= max_use:
                break
            used += 1
        if used <= max_use:
            count += 1
        else:
            break

    return count


if __name__ == "__main__":
    hurt_finger = int(input())
    max_use = int(input())
    print(count_max_numbers(hurt_finger, max_use))

