n=int(input())
words=[]
for i in range(n):
    word=input()
    words.append(word)

chr=input()
tot, cnt=0,0
for i in words:
    if i[0]==chr:
        tot+=len(i)
        cnt+=1

print(f'{cnt} {tot/cnt:.2f}')