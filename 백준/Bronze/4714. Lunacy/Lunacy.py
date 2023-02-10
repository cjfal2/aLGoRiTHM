import sys
input = sys.stdin.readline

while 1:
    num = float(input().strip())
    if num < 0:
        break
    new = 0.167 * num
    print(f'Objects weighing {num:.2f} on Earth will weigh {new:.2f} on the moon.')
    
    