# n = int(input())
# nums = list(map(int, input().split()))

# # Write your code here!
# for i in nums:
#     if nums.count(i)==2 or nums.count(i)>2:
#         while i in nums:
#             nums.remove(i)

  
# if nums==[]:
#     print(-1)
# else:
#     print(max(nums))

n = int(input())
nums = list(map(int, input().split()))

# 등장 횟수를 저장할 딕셔너리 생성
count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

# 등장 횟수가 1번인 숫자만 남기기
filtered_nums = [num for num in nums if count[num] == 1]

# 결과 출력
if filtered_nums:
    print(max(filtered_nums))
else:
    print(-1)
