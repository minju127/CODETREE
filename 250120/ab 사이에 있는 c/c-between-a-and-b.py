a,b,c=list(map(int, input().split(' ')))
nums=False
for i in range(a, b+1):
    if i%c==0:
        nums=True

if nums==True:
    print('YES')
else:
    print('NO')