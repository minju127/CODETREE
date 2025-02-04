arr=list(map(int, input().split()))
arr2=[]

for i in arr:
    if i==0:
        break
    else:
        if i%2==0:
            arr2.append(i)

print(f'{len(arr2)} {sum(arr2)}')