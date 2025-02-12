n, m = map(int, input().split())

#행 : n / 열 : m
# Write your code here!
arr=[
    [0 for j in range(m)]
    for i in range(n)
]
cnt=0
for i in range(m):
    if i%2==0:
        for j in range(n):
            arr[j][i]=cnt
            cnt+=1
    else:
        for j in range(n-1, -1, -1):
            arr[j][i]=cnt
            cnt+=1

for row in arr:
    for num in row:
        print(num, end=' ')
    print()