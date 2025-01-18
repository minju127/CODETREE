n=int(input())
tot=1
for i in range(1, 11):
    tot*=i
    if tot>=n:
        print(i)
        break