letter=input()

words=['apple','banana','grape','blueberry','orange']

cnt=0
for i in words:
    if letter==i[2] or letter==i[3]:
        cnt+=1
        print(i)
print(cnt)