a,b=list(map(int, input().split(' ')))
tot=0
for i in range(a, b+1):
    tot+=i
print(tot)