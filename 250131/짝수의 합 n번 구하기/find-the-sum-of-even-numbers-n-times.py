n=int(input())

for i in range(n):
    a,b=map(int, input().split(' '))
    sums=0
    for j in range(a, b+1):
        if j%2==0:
            sums=sums+j
    print(sums)