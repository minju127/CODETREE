n=int(input())

for i in range(1, n+1):  #아래 코드 3번 반복
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(1,n):
    for j in range(n-i):
        print('*', end=' ')
    print()