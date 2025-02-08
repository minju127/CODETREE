arr=list(map(int, input().split()))

max_val=arr[0]
min_val=arr[0]
for i in arr[1:]:
    if i==999 or i==-999:
        break
    if max_val>i:
        max_val=max_val
    else:
        max_val=i

    if min_val>i:
        min_val=i
    else:
        min_val=min_val

print(f'{max_val} {min_val}')