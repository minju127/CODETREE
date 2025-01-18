n=int(input())
cnt=0
num=1
while True:
    n=n/num
    cnt+=1
    num+=1
    if n<=1:
        cnt-=1
        break
print(cnt)