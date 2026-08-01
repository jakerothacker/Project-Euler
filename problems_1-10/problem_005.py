#smallest number that can be divided by 1-20

from prime_function_stroage import is_prime

def smallest_number_divisible_by_1_to_n(n):
    """Finds the smallest number that can be divided by all numbers from 1 to n

    Args:
        n (int): The upper limit

    Returns:
        int: The smallest number divisible by all numbers from 1 to n

    Requires:
        is_prime(n): from prime_function_stroage.py
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    prime_powers = []
    for prime in primes:
        power = 1
        while prime ** power <= n:
            power += 1
        prime_powers.append(power-1)
    product = 1
    for i in range(len(primes)):
        product *= primes[i] ** (prime_powers[i])
    return product

print(smallest_number_divisible_by_1_to_n(20))
