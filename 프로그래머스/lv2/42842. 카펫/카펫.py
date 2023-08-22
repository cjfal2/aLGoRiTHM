import math

def solution(brown, yellow):
    return [
        (-1 + (brown / 4) + math.sqrt(1 - (brown / 2) + (brown * brown / 16) - yellow)) + 2,
        (-1 + (brown / 4) - math.sqrt(1 - (brown / 2) + (brown * brown / 16) - yellow)) + 2
    ]