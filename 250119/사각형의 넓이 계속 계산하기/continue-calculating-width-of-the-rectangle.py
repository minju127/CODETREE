area=[]
while True:
    lists=input().split(' ')
    area.append(int(lists[0])*int(lists[1]))
    if lists[-1]=='C':
        break

for i in area:
    print(i)
    