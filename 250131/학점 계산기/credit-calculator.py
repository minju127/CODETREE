n=int(input())

score=list(map(float, input().split()))
#mn=sum(score)/len()
print(f'{sum(score)/len(score):.1f}')

if sum(score)/len(score)>=4.0:
    print('Perfect')
elif sum(score)/len(score)>=3.0:
    print('Good')
else:
    print('Poor')