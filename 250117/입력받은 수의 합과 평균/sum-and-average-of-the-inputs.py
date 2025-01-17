n=int(input())
tot=0
for _ in range(n):
    a=int(input())
    tot+=a

print(f'{tot} {tot/n:.1f}')