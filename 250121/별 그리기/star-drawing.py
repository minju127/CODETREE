n = int(input())  #n=5
#가로, 세로 5*5
#_ _ * _ _
#_ * * * _
#* * * * *
#_ * * * _
#_ _ * _ _

# Write your code here!
for i in range(1, n+1):  #1,2,3
    for j in range(n-i):
        print(' ', end='')
    
    for k in range(2*i-1):  #1,3,5
        print('*', end='')
    print()

for i in range(1, n):  #1,2,3,4
    for j in range(i):
        print(' ', end='')
    
    for k in range(n*2-(i*2+1)):   
        print('*', end='')
    print()