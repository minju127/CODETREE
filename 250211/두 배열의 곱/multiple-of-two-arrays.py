arr_1=[
    list(map(int, input().split())) for i in range(3)
]
#↑ 여기서는 입력값을 최종적으로 list로 묶어주기 때문에 전 문제랑은 달리 다시 []로 묶어주지 않아도 됨
_=input()
#중간에 줄 간격도 입력으로 들어오기 때문에 따로 처리해줘야 됨
arr_2=[
    list(map(int, input().split())) for j in range(3)
]

tot_arr=[]
for i in range(3):  #0 1 2
    row=[] #for문 안쪽에서 row를 빈 리스트로 지정해주지 않으면 row에 이전 계산값이 저장된 상태로 계속 append가 됨
    for j in range(3):  #0 1 2
        row.append(arr_1[i][j] * arr_2[i][j])
    tot_arr.append(row)

for rows in tot_arr:
    for num in rows:
        print(num, end=' ')
    print()