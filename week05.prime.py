def is_prime(number : int) -> bool:
    """
    Function to determine whether a number is a prime number.
    :param number: The number to determine whether it is prime or not.
    :return: Returns True if it is a prime number, False if it is not.
    """

    if number < 2:  # Numbers less than 2 are not prime
        return False

    for i in range(2, int(number ** 0.5) + 1):  # Loop to check divisors up to the square root of the number
        if number % i == 0:  # If divisible, not a prime number
            return False

    return True

number1 = int(input("숫자를 입력하세요: "))
number2 = int(input("숫자를 입력하세요: "))

if number1 > number2:
    number1, number2 = number2, number1

for i in range(number1, number2+1):
    if is_prime(i):
        print(i, end=" ")
"""if is_prime(number):
    print(f"\n{number}는(은) 소수입니다.")
else:
    print(f"\n{number}는(은) 소수가 아닙니다.")"""
