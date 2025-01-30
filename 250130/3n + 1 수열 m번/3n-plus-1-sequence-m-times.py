m=int(input())
for i in range(m):
    cnt=0
    n=int(input())
    while True:
        if n==1:
            print(cnt)
            break
        if n%2==0:
            n=n//2
            cnt+=1
        elif n%2!=0:
            n=n*3+1
            cnt+=1