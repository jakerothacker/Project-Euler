#sum of primes (below two million)
from prime_function_stroage import next_prime


def sum_primes(n):
    """Summs the primes below n

    Args:
        n (int): highest possible prime to be added

    Requires:
        next_prime from prime_function_storage
    
    """
    prime = 2
    sum = 0
    while prime < n:
        sum += prime
        prime = next_prime(prime)

    return(sum)

print(sum_primes(2000000))