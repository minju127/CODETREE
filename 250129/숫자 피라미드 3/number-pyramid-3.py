n=int(input())

for i in range(1, n+1): #1,2,3,4
    for j in range(i):
        print(i*(j+1), end=' ')
    print()