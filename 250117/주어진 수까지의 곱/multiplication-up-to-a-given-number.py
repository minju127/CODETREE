a,b=list(map(int, input().split(' ')))
tot=1
for i in range(a, b+1):
    tot*=i
print(tot)