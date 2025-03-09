num=int(input())
tot, a_1=0,0
for i in range(num):
    word=input()
    tot+=len(word)
    if word[0]=='a':
        a_1+=1

print(f'{tot} {a_1}')