n=int(input())

for i in range(1, n+1):  #4번반복
    for j in range(i):
        print('*', end='')
    print()
    print()

for i in range(1, n):  #1,2,3
    for j in range(n-i):  #3,2,1
        print('*', end='')
    print()
    print()