arr_2d=[
    list(map(int, input().split()))
    for _ in range(4)
]  #2차원 배열

sums=0
for i in range(4):
    for j in range(i+1):
        sums=sums+arr_2d[i][j]

print(sums)