n = int(input())
prime=[]

for num in range(2, n + 1): #1은 소수가 아님
    is_prime = True
    
    for i in range(2, num):  #어짜피 모든 수는 1로 나눠 떨어지므로 굳이 1부터 시작할 필요가 없음
        if num % i == 0:
            is_prime = False
            #2 ~ num-1까지의 수 중 나머지가 0이 되는 수가 있는 즉시 소수가 될 수 없으므로
            #break를 걸어준다!
            break
    
    #안의 for문이 끝난 다음 여전히 is_prime이 True라면 count를 해줌
    if is_prime:
        prime.append(num)

for i in prime:
    print(i, end=' ')