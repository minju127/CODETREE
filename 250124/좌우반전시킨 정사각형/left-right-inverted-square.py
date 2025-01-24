n = int(input())

for i in range(1, n + 1):  # 바깥쪽 루프 (행)
    for j in range(n, 0, -1):  # 안쪽 루프 (열)
        print(i * j, end=" ")  # i와 j를 곱한 값 출력
    print()  # 줄바꿈



#i*j

#-