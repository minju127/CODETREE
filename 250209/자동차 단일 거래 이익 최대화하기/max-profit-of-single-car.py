n = int(input())  #N년
price = list(map(int, input().split()))   #N년의 가격들

money=[]
# Write your code here!
for i in range(n): #0 1 2 3 4
    for j in price[i:]:
        if price[i]<j:
            money.append(j-price[i])

if money:
    print(max(money))
else:
    print(0)