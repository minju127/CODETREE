arr=[0,0,0,0,0]
for i in range(3):
    a,b=input().split()
    if a=='Y' and int(b)>=37:
        arr[1]+=1
    if a=='N' and int(b)>=37:
        arr[2]+=1
    if a=='Y' and int(b)<37:
        arr[3]+=1
    if a=='N' and int(b)<37:
        arr[4]+=1


for i in arr[1:]:
    print(i, end=' ')

if arr[1]>=2:
    print('E')
