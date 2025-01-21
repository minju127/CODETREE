n=int(input())

for i in range(0, n):   #0, 1, 2, 3
    for j in range(n-i):
        print('*', end='')
    
    for k in range(2*i):   #0, 2, 4, 6
        print(' ', end='')
    
    for y in range(n-i):
        print('*', end='')
    print()