arr=list(map(int, input().split()))

nums=[0,0,0,0,0,0,0,0,0,0]

for i in arr:
    if i==0:
        break
    nums[i//10]+=1

for i in range(1,10):
    print(f'{i} - {nums[i]}')