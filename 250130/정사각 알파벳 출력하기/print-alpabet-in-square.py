#ord() : 아스키 코드
#chr() : 알파벳
n=int(input())
cnt=0
for i in range(n):
    for j in range(n):
        print(chr(ord('A')+cnt), end='')
        cnt+=1
    print()