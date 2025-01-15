a=int(input())
classroom=0
street=0
bath=0

for i in range(1,a+1):
    if i%12==0:
        bath+=1
    elif i%3==0:
        street+=1
    elif i%2==0:
        classroom+=1

print(f'{classroom} {street} {bath}')