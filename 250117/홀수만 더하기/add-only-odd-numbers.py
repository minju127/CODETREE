n=int(input())
tot=0
for i in range(n):
    a=int(input())
    if a%2!=0 and a%3==0:
        tot+=a

print(tot)