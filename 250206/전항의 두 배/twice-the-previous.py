a,b=list(map(int, input().split()))

arr=[a,b,0,0,0,0,0,0,0,0]

for i in range(2,10):
    arr[i]=arr[i-1] + 2*arr[i-2]

for i in arr:
    print(i, end=' ')