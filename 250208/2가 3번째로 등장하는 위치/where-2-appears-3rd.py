n=int(input())
n_arr=list(map(int, input().split()))

cnt=0
when=0
for i in n_arr:
    if i==2:
        cnt+=1
    when+=1

    if cnt==3:
        break

print(when)