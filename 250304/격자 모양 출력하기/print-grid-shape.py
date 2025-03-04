n,m=list(map(int, input().split()))
#n:격자의 크기 / m:점의 개수 (for문으로 반복할 횟수)

arr=[
    [0 for j in range(n)]
    for i in range(n)
]

for i in range(m):
    (r,c)=tuple(map(int, input().split()))
    arr[r-1][c-1]=r*c


for nums in arr:
    for num in nums:
        print(num, end=' ')
    print()
