'''
https://www.acmicpc.net/problem/16198
'''

N = int(input())
arr = list(map(int, input().split()))
# temp = []

answer = 0 # 최소값으로 0을 설정

def back(temp, hap):
    global answer
    
    if len(temp) == 2:
        answer = max(hap, answer)
        return

    for i in range(1, len(temp)-1): # 양쪽은 불가능
        side_gop = temp[i-1] * temp[i+1]
        num = temp.pop(i)
        back(temp, hap+side_gop)
        temp.insert(i, num)

back(arr, 0)
print(answer)