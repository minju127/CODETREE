n = int(input())
cnt = 1  # 첫 번째 숫자

for i in range(n):
    if i % 2 == 0:  # 짝수 행
        for j in range(n):
            print(cnt, end=' ')
            cnt += 1  # 1씩 증가
    else:  # 홀수 행
        cnt += 1  # 짝수 행의 끝 값 +2로 시작
        for j in range(n):
            print(cnt, end=' ')
            cnt += 2  # 2씩 증가
    print()  # 줄바꿈
    if i % 2 != 0:  # 홀수 행 이후, 짝수 행을 준비하기 위해 cnt 조정
        cnt -= 1  # 다음 짝수 행에서 연속되도록 조정


