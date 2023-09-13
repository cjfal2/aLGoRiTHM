import heapq

def solution(operations):
    answer = []
    for command in operations:
        i, j = command.split(" ")
        j = int(j)
        if i == "I":
            heapq.heappush(answer, j)
        else:
            if not answer:
                continue
                
            if j == -1:
                heapq.heappop(answer)
            else:
                answer = list(map(lambda x: x * -1, answer))
                heapq.heapify(answer)
                
                heapq.heappop(answer)
                
                answer = list(map(lambda x: x * -1, answer))
                heapq.heapify(answer)
    return [max(answer), min(answer)] if answer else [0, 0]