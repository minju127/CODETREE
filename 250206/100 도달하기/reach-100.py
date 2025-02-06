n=int(input())

arr=[1,n]
i=2
while True:
    num=arr[i-1]+arr[i-2]
    arr.append(num)
    i+=1
    if num>100:
        break

for i in arr:
    print(i, end=' ')