arr=list(map(int, input().split()))

min_500=[]
max_500=[]

for i in arr:
    if i>500:
        max_500.append(i)
    elif i<500:
        min_500.append(i)

print(f'{max(min_500)} {min(max_500)}')