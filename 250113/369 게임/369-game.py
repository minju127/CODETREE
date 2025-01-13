n=input()
for i in range(1, int(n)+1):
    if i%3==0:
        print(0, end=' ')
    elif ('3' in i) or ('6' in i) or ('9' in i):
        print(0, end=' ')
    else:
        print(i)