maskW, maskB = map(int, input().split())
shirtW, shirtB = map(int, input().split())
pantsW, pantsB = map(int, input().split())

# 각각의 세트에서 최소값을 구함
set1_min = min(maskW, shirtB, pantsW)
set2_min = min(maskB, shirtW, pantsB)

# 결과 출력
if set1_min == set2_min:
    print(set1_min * 2)
else:
    print(min(set1_min, set2_min) * 2 + 1)