n=int(input())
cnt=0
for i in range(1, n+1):
    for j in range(i):
        if ord('A')+cnt > ord('Z'):
            cnt=0

        print(chr(ord('A')+cnt),end='')
        cnt+=1
    print()