a,b=list(map(int, input().split(' ')))
tot, cnt=0, 0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        tot+=i
        cnt+=1

print(f'{tot} {tot/cnt:.1f}')