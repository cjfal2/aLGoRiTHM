def solution(arr1, arr2):
    N = len(arr1)    # 앞에거 세로길이
    M = len(arr2[0]) # 뒤에거 가로길이
    K = len(arr1[0]) # 앞에거 가로길이
    
    answer = [[0 for _ in range(M)] for _ in range(N)]
    
    for n in range(N): 
        for m in range(M): 
            for k in range(K): 
                answer[n][m] += arr1[n][k] * arr2[k][m]
    return answer