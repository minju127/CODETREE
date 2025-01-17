nums=[]
for _ in range(10):
    a=int(input())
    nums.append(a)

tot,cnt=0,0
for i in nums:
    if i>=0 and i<=200:
        tot+=i
        cnt+=1
print(f'{tot} {tot/cnt:.1f}')