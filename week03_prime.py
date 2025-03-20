number = int(input("숫자를 입력하세요: "))
is_prime = True

if number >= 2:  # 조건문 끝에 콜론(:) 사용
    for i in range(2, number):
        if number % i == 0:
            is_prime = False  # 들여쓰기 수정
            print(i, end=" ")  # 약수를 출력
else:
    is_prime = False  # 변수 이름 수정

if is_prime:  # 변수 이름 수정
    print(f"\n{number}는(은) 소수입니다.")  # print 문법 수정
else:
    print(f"\n{number}는(은) 소수가 아닙니다.")  # print 문법 수정