def is_prime(number):
    """
    Function to determine whether a number is a prime number
The number to determine whether it is prime or not
    :param number:
    :return: Returns true if it is a prime number, False if it is not a prime number.
    """


number = int(input("숫자를 입력하세요: "))
is_prime = True

if number >= 2:  # 숫자가 2 이상인 경우에만 검사
    i = 2
    while i * i <= number:
        if number % i == 0:
            is_prime = False  # 소수가 아님을 표시
        print(i, end=" ")  # 약수 출력
        i = i + 1  # 항상 i를 증가시킴
else:
    is_prime = False 

if is_prime:
    print(f"\n{number}는(은) 소수입니다.")
else:
    print(f"\n{number}는(은) 소수가 아닙니다.")
