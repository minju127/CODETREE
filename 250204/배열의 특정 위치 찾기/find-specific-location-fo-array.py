arr=list(map(int, input().split()))
sums=0
avg=0
for i in range(1,10,2):
    sums+=arr[i]

for i in range(2,10,3):
    avg+=arr[i]


print(f'{sums} {avg/3:.1f}')