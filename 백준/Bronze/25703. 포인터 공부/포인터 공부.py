n=int(input())+1
print("int a;")
print('int *ptr = &a;')


for i in range(2, n):
    star = "*"*i
    print(f'int {star}ptr{i} = &ptr{i-1};') if i!=2 else print(f'int {star}ptr{i} = &ptr;')