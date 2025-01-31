start, end = map(int, input().split())

# Write your code here!
cnt=0
for i in range(start, end+1):#3 4 5 6 7 8 9 ...
    sums=0
    for j in range(1, i):  #1,2,3,4,5.....
        if i%j==0:
            sums=sums+j
    if i==sums:
        cnt=cnt+1
    

print(cnt)