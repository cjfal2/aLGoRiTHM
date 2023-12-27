def solution(price):
    if price < 100000:
        return int(price)
    if 300000 > price >= 100000:
        return int(price*0.95)
    if 500000 > price >= 300000:
        return int(price*0.9)
    return int(price*0.8)