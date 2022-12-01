import sys


def mixing():
    '''
    pH: 섞은 용액의 가장 0에 가까운 특성 값
    basic: -쪽 용액의 포인터 염기성
    acidic: +쪽 용액의 포인터 산성
    '''
    pH, basic, acidic = sys.maxsize, 0, N -1
    while (basic < acidic): # 염기성이 산성보다 커지면 종료
        mix = liquid[basic] + liquid[acidic] # 염기성과 산성을 섞어봄

        if pH > abs(mix): # pH 보다 mix가 0에 가까우면
            pH, neutral_small, neutral_large = abs(mix), liquid[basic], liquid[acidic]
            # pH를 갱신하고, 중성작은거, 중성큰거를 저장
            if not mix: # 만약 0이면 바로 종료
                break

        if mix < 0: # mix가 0보다 작으면 염기성 포인터를 옮겨봄
            basic += 1
        else: # mix가 0보다 크면 산성 포인터를 옮겨봄
            acidic -= 1
    return [neutral_small, neutral_large]


# 인풋 받고 바로 솔트 때려주고요 (이진탐색을 위해)
N = int(input())
liquid = sorted(list(map(int, input().split())))
if liquid[0] >= 0:
    print(liquid[0], liquid[1])
    quit()
if liquid[-1] <= 0:
    print(liquid[N-2], liquid[N-1]) 
print(*mixing()) # 중성작은거, 중성큰거를 출력
