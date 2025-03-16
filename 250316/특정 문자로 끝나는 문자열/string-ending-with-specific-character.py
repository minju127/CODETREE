words=[]
for i in range(10):
    word=input()
    words.append(word)

a=input()
cnt=0
for i in words:
    if i[-1]==a:
        print(i)
        cnt+=1
if cnt==0:
    print('None')