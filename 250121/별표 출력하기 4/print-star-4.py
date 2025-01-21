n=int(input())

for i in range(n):  #3번 반복 0,1,2
    for j in range(n-i):
        print('*', end=' ')
    print()

for i in range(2, n+1):  #(2, 4)  2,3
    for j in range(i):
        print('*', end=' ')
    print()