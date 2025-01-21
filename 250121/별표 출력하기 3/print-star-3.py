n=int(input())  #n=3

for i in range(n):  #0,1,2
    for j in range(i*2):
        print(' ', end='')
    
    for k in range(2*n - (i*2+1)):
        print('*', end=' ')
    print()


    #5,3,1
    #3*2-1  3*2-3   3*2-5