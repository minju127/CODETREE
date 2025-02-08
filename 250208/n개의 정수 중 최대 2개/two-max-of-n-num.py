n = int(input())
a = list(map(int, input().split()))

# Write your code here!
a.sort()

print(f'{a[-1]} {a[-2]}')