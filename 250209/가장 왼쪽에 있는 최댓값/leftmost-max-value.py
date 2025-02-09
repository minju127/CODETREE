# n = int(input())
# a = list(map(int, input().split()))

# # Write your code here!
# while True:
#     print(a.index(max(a))+1, end=' ')
#     a=a[0:a.index(max(a))]
#     #↑ 최댓값의 왼쪽 범위 슬라이싱으로 다시 a에 저장! (작아진 범위에서 다시 최댓값을 찾아야 되니까)
#     if a.index(max(a))+1==1:
#         #index()는 우리가 아는 리스트 인덱스로 나오는데 문제에서는 몇"번째"니까 +1
#         #리스트의 0번 인덱스 = 첫번째 원소
#         #만약에 제일 왼쪽(범위의 첫번째)값이 최대값이면 1을 출력하고 break
#         print(1)
#         break

n = int(input())
a = list(map(int, input().split()))

while a:  # a가 비어있지 않을 때만 반복
    print(a.index(max(a)) + 1, end=' ')
    a = a[:a.index(max(a))]
