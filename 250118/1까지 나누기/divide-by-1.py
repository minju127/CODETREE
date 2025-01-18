n=int(input())
cnt=0
num=1
while True:
    n=n/num
    num+=1
    if n<=1:
        break
    cnt+=1
print(cnt)