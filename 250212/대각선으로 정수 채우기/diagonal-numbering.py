nm = input().split()
n, m  = int(nm[0]), int(nm[1])
arr = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

# 대각선의 값을 k라고 했을 때, i, j의 합이 k가 되는 규칙을 적용해봤습니다. 
# k = 0일 때는 i = j = 0일 때 채워주고, k = 1일 때는 (0,1), (1,0) 순으로 채워주는 방식입니다. 
for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr[i][j] = cnt
                cnt += 1


for row in arr:
    for elem in row:
        print(elem, end = " ")
    print()
