ages=[]
cnt=0
while True:
    age=int(input())
    if age>29 or age<=19:
        break
    ages.append(age)
    cnt+=1
avgs=sum(ages)/cnt
print(f'{avgs:.2f}')