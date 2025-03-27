def is_prime(number):
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

    return True  # If no divisors found, the number is prime


number = int(input("숫자를 입력하세요: "))
if is_prime(number):
    print(f"\n{number}는(은) 소수입니다.")
else:
    print(f"\n{number}는(은) 소수가 아닙니다.")
