a,b=list(map(int, input().split(' ')))
tot=0
for i in range(a, b+1):
    if i%6==0 and i%8!=0:
        tot+=i
print(tot)