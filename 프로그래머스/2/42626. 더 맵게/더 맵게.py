import heapq


def solve(first, second):
    return first + (second * 2)
    
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    a = heapq.heappop(scoville)
    if a >= K:
        return 0
    heapq.heappush(scoville, a)
    while 1:
        if len(scoville) < 2:
            return -1
        
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = solve(a, b)
        heapq.heappush(scoville, c)
        d = heapq.heappop(scoville)
        if d >= K:
            break
        else:
            heapq.heappush(scoville, d)
    return answer