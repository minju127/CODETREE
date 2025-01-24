n=int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n:
            print('*', end=' ')

        elif j==1 or j==n:
            print('*', end=' ')

        elif j<i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
        
    print()

#   1 2 3 4 5
# 1 * * * * *
# 2 *       *
# 3 * *     *
# 4 * * *   *
# 5 * * * * * 