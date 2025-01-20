n=int(input())   #n=3
for i in range(0, n):  #3번 돌아감  i= 0 / 1 / 2
    for j in range(n-i):
        print('*', end=' ')
    print()