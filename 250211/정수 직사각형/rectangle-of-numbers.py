n,m=list(map(int, input().split()))

arr_2d=[
    [0 for j in range(m)]
    for i in range(n)
]
#이중 for문이니까 안에 []을 한 번 더 해줘야 됨

num=1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num+=1

for row in arr_2d:
    for value in row:
        print(value, end=' ')
    print()