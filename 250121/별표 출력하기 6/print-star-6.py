n=int(input())  #3

for i in range(0, n):  # 0, 1, 2 (i)
    for j in range(i):
        print(' ', end=' ')
    
    for k in range(2*n - (2*i+1)):   #5, 3, 1
        print('*', end=' ')
    print()
    
for i in range(1, n):  # i = 1,2
    for k in range(n-(i+1)):    #1,0
        print(' ', end=' ')

    for j in range(2*i +1):  #3,5,7
        print('*', end=' ')
    print()