n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
for i in nums:
    if nums.count(i)>=2:
        while i in nums:
            nums.remove(i)

  
if nums==[]:
    print(-1)
else:
    print(max(nums))
    