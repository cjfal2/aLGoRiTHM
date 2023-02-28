def solution(board, moves):
    answer = 0
    N = len(board)
    stack = []
    for i in moves:
        i -= 1
        for n in range(N):
            if board[n][i]:
                if len(stack) > 0 and stack[-1] == board[n][i]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[n][i])
                board[n][i] = 0
                break
    
    return answer