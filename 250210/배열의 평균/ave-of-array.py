arr_2d=[
    list(map(int, input().split()))
    for _ in range(2)
]

#[[10 20 30 40]
# [50 60 70 80]]   [0][0] + [1][0] / [0][1] + [1][1]

for i in range(2):
    print(f'{sum(arr_2d[i])/4:.1f}', end=' ')
print()

for i in range(4): #0 1 2 3
    sums=0
    for j in range(2): #0 1
        sums+=arr_2d[j][i]
    print(f'{sums/2:.1f}', end=' ')
print()

tot=0
for i in range(2):
    tot+=sum(arr_2d[i])
print(f'{tot/8:.1f}')