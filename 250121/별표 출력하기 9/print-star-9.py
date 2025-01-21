n=int(input())
for i in range(1, n+1):
    for j in range(n-i):  #공백 개수 2, 1, 0  (end=' '로 붙이면!)
        print(' ', end=' ')
    
    for k in range(2*i-1):  #1, 
        print('*', end=' ')
    print()