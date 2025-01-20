n=int(input())
for i in range(1, n+1):  # 1, 2, 3, 4, 5
    for j in range(2*i-1):   # 1, 3, 5, 7, 9
        print('*',end='')
    print()