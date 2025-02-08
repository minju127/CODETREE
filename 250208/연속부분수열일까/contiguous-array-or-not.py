len_A, len_B=list(map(int, input().split()))  #len_B=2

arr_A=list(map(int, input().split()))
arr_B=list(map(int, input().split()))  

yes=False
for i in range(len_A-len_B+1):  #len_A - len_B의 길이만큼 반복 0,1,2 (3번)
    if arr_A[i:len_B+i]==arr_B:  #[0:2]  [1:3] [2:4]
        yes=True

if yes:
    print('Yes')
else:
    print('No')
