a,b=list(map(int, input().split(' ')))
tot=1
for i in range(1, b+1):
    if i%a==0:
        tot*=i
print(tot)