#largest prime factor of 600851475143
import math

def next_prime(n):
    """Finds the next highest prime number

    Args:
        n (int): any positive integer.
    """
    if n==2:
        return (3)
    possible_prime = n + 1
    while True:
        for i in range (2,math.ceil(possible_prime**0.5)+1):
            if possible_prime % i == 0:
                possible_prime += 1 
                break
            elif i==math.ceil(possible_prime**0.5):
                return(possible_prime)

def list_of_prime_factors(n):
    """Creates a list of prime factors of n

    Args:
        n (int): any positive integer
    """
    check_prime = 2
    prime_factors = [1]
    while check_prime < math.ceil(n/2):
        if n % check_prime == 0:
            prime_factors.append(check_prime)

            product = 1 #short cut for some numbers
            for num in prime_factors:
                product = product*num
            if product == n:
                return prime_factors

        check_prime = next_prime(check_prime)
    return(prime_factors)

print(list_of_prime_factors(600851475143))
