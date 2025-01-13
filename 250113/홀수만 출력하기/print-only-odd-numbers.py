n=int(input())
nums=[]
for i in range(n):
    a=int(input())
    nums.append(a)

for y in nums:
    if y%2==1 and y%3==0:
        print(y)