n=int(input())
hap=False
for i in range(2, n):
    if n%i==0:
        hap=True
if hap==True:
    print('C')
else:
    print('N')