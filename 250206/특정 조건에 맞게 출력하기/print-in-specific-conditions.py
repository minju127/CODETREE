arr=list(map(int, input().split()))
sums=0
for i in arr:
    if i==0:
        break
    else:
        if i%2==0:
            print(i//2, end=' ')
        else:
            print(i+3, end=' ')