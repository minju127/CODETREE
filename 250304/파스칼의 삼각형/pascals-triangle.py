n=int(input())

arr=[
    [0 for j in range(i)]
    for i in range(1, n+1)
]

for i in range(n):
    arr[i][0]=1
    arr[i][i]=1

for i in range(2, n):
    for j in range(1, i):
        arr[i][j]=arr[i-1][j-1] + arr[i-1][j]

for nums in arr:
    for num in nums:
        print(num, end=' ')
    print()