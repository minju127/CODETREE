nums=[]
for i in range(5):
    a=int(input())
    nums.append(a)
sat=True
for i in nums:
    if i%3!=0:
        sat=False

if sat==True:
    print(1)
else:
    print(0)