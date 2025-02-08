arr=list(map(int, input().split()))

max_val=0

for i in arr:
    if max_val>i:
        max_val=max_val
    else:  #max_val<i
        max_val=i

print(max_val)