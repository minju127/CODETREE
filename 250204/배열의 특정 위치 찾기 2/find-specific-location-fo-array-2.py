arr=list(map(int, input().split()))
sums_1=0
sums_2=0

for i in arr[0:10:2]:
    sums_1+=i

for j in arr[1:10:2]:
    sums_2+=j

if sums_1>sums_2:
    print(sums_1-sums_2)
else:
    print(sums_2-sums_1)