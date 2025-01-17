#약수는 꼭 소수만을 의미하는게 아님!
#e.g. 12의 약수는 1,2,3,4,6,12임
n=int(input())
tot=0
for i in range(1,n):
    if n%i==0:
        tot+=i

if tot==n:
    print('P')
else:
    print('N')