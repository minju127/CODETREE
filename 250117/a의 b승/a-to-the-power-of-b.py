a,b=list(map(int, input().split(' ')))
tot=1
for _ in range(b):
    tot*=a
print(tot)