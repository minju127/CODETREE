n=int(input())

for i in range(n, 0, -1):
    for j in range(n):
        print(f'({i},{n-j})', end=' ')
    print()