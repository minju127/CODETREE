N, Q=list(map(int, input().split()))
main_arr=list(map(int, input().split()))  #질의 수행 대상 array

for i in range(Q):  #Q개의 줄에 거쳐 Q개의 질의가 들어옴
    question=list(map(int, input().split()))  #질의 1 1 형태
    if question[0]==1 or question[0]==2:
        qq=question[0]  #질의 부분만 뽑아서 qq에 담기
        what_qq=question[1]  #질의에서 숫자 부분
    else:  #3번 질의인 경우
        qq=question[0]
        start=question[1]
        end=question[2]

    if qq==1:
        print(main_arr[what_qq-1])
    elif qq==2:
        if what_qq in main_arr:
            print(main_arr.index(what_qq)+1)
        else:
            print(0)
    elif qq==3:
        for i in range(start-1, end):
            print(main_arr[i], end=' ')
        print()



