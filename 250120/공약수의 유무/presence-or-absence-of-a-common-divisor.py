a,b=list(map(int, input().split(' ')))
comm=False
for i in range(a, b+1):
    if 1920%i==0 and 2880%i==0:
        comm=True

if comm==True:
    print(1)
else:
    print(0)