# n=int(input())
# cnt=1
# for i in range(n):
#     for j in range(n):
#         if i%2==0:
#             print(cnt, end=' ')
#             cnt+=1
#         else:
#             cnt=n*(i+1)
#             print(cnt-j, end=' ')
            
#     print()

n = int(input())  # 자연수 n
num = 1  # 출력할 숫자 시작 값

for i in range(n):
    if i % 2 == 0:  # 짝수 번째 행
        for j in range(n):
            print(num, end=" ")
            num += 1
    else:  # 홀수 번째 행
        start = num + n - 1  # 현재 행의 숫자 시작 값
        for j in range(n):
            print(start, end=" ")
            start -= 1
        num += n  # 다음 숫자 값 업데이트
    print()  # 행이 끝날 때 줄바꿈
