a,b=list(map(int, input().split()))
arr=[0]*b
while True:
    c=a%b #c는 나머지
    arr[c]+=1
    a=a//b
    if a<=1:
        break

sums=0
for i in arr:
    sums=sums+(i**2)

print(sums)