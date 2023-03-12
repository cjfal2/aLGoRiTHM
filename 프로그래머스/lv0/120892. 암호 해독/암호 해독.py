def solution(cipher, code):
    answer = ''
    for idx, word in enumerate(list(cipher), 1):
        if not idx%code:
            answer += word
            
    return answer