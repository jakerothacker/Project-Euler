#nth prime number
from prime_function_stroage import is_prime
def nth_prime(n):
    """Finds the nth prime number

    Args:
        n (int): The position of the prime number to find

    Returns:
        int: The nth prime number
    """
    if n == 1:
        return 2
    if n == 2:
        return 3
    count = 2
    num = 5
    while True:
        if is_prime(num):
             count += 1
        if count == n:
            return num
        num += 2

print(nth_prime(10001))