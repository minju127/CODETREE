n=int(input())

for i in range(n):
    for j in range(n):
        if i%2==0 and j%2==0:
            print(i+1, end='')
        elif i%2==0 and j%2!=0:
            print(n-i, end='')
        elif i%2!=0 and j%2!=0:
            print(n-i, end='')
        elif i%2!=0 and j%2==0:
            print(i+1, end='')
    print()