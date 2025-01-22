n=int(input())  #n=3

for i in range(2*n):
    if i %2==0:  #i가 짝수면 0,2,4
        for j in range(n-(i//2)):
            print('*', end=' ')
        print()
    else:  #i가 홀수면 1,3,5
        for j in range(1+(i//2)):
            print('*', end=' ')
        print()