n=int(input())
tot=0
for i in range(1, 101):
    tot+=i
    if tot >=n:
        print(i)
        break