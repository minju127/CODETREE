n=int(input())
arr=list(map(int, input().split()))

nums=[0]*10
for i in arr:
    nums[i]+=1

for i in nums[1:]:
    print(i)