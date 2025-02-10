arr_2d=[
    list(map(str.upper, input().split()))
    for _ in range(5)
]
#upper()는 리스트에서 사용할 수 없음

for i in range(5):
    for j in arr_2d[i]:
        print(j, end=' ')
    print()


# arr_2d = [
#     [word.upper() for word in input().split()]
#     for _ in range(5)
# ]
