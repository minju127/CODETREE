scores=list(map(int, input().split()))

nums=[0,0,0,0,0,0,0,0,0,0,0]

for i in scores:
    if i==0:
        break
    nums[i//10]+=1

for i in range(10,0,-1):
    print(f'{i*10} - {nums[i]}')