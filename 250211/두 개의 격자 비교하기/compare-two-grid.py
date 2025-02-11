n,m=list(map(int, input().split()))

arr_1=[
    list(map(int, input().split())) for i in range(n)
]

arr_2=[
    list(map(int, input().split())) for j in range(n)
]

tot_arr=[]
for i in range(n):
    new_arr=[]
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            new_arr.append(0)
        else:
            new_arr.append(1)
    tot_arr.append(new_arr)

for row in tot_arr:
    for nums in row:
        print(nums, end=' ')
    print()
