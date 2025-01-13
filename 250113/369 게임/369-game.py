n=input()
for i in range(1, int(n)+1):
    if i%3==0:
        print(0, end=' ')
    elif '3' in n or '6' in n or '9' in n:
        print(0, end=' ')
    else:
        print(i)