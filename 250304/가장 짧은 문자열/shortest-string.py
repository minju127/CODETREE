a=len(input())
b=len(input())
c=len(input())

num1=abs(a-b)
num2=abs(a-c)
num3=abs(b-c)

arr=[]
arr.append(num1)
arr.append(num2)
arr.append(num3)

print(max(arr))
