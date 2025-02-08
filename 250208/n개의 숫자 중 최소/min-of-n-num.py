n = int(input())
a = list(map(int, input().split()))

# Write your code here!
min_val=a[0]

for i in a[1:]:
    if min_val<i:
        min_val=min_val
    else: #min_val>i
        min_val=i

print(min_val, a.count(min_val))