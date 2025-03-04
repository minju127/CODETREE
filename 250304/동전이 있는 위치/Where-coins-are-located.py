n,m=list(map(int, input().split()))
#n:격자 크기 / m:동전의 개수

arr=[
    [0 for j in range(n)]
    for i in range(n)
]

for i in range(m):
    (r,c)=tuple(map(int, input().split()))
    arr[r-1][c-1]=1


for nums in arr:
    for num in nums:
        print(num, end=' ')
    print()