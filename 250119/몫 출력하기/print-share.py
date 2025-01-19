nums=[]
cnt=0
while True:
    a=int(input())
    nums.append(a)
    if a%2==0:
        cnt+=1
    if cnt==3:
        break

for num in nums:
    if num%2==0:
        print(num//2)