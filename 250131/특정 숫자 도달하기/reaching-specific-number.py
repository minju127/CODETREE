# nums=list(map(int, input().split()))
# sums=0
# cnt=0
# for i in nums:
#     sums=sums+i
#     cnt+=1
#     if i>=250:
#         sums=sums-i
#         cnt-=1
#         print(f'{sums} {sums/cnt}')
#         break
    
# print(f'{sums} {sums/cnt}')

nums = list(map(int, input().split()))
sums = 0
cnt = 0

for i in nums:
    if i >= 250:
        break
    sums += i
    cnt += 1

print(f'{sums} {sums/cnt}')
