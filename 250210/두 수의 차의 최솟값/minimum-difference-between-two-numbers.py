n=int(input())
arr=list(map(int, input().split()))
minus=[]
for i in range(n):  #0 1 2 3 
    for j in arr[i+1:]:  #1 2 3 4
        minus.append(abs(arr[i]-j))
print(min(minus))