arr=list(map(int, input().split()))
arr2=[]
for i in arr:
    if i==0:
        break
    else:
        arr2.append(i)

for j in arr2[::-1]:
    print(j, end=' ')