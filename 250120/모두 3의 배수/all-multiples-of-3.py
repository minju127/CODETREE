nums=list(map(int, input().split(' ')))
sat=True
for i in nums:
    if i%3!=0:
        sat=False

if sat==True:
    print(1)
else:
    print(0)