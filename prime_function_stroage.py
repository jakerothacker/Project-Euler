import math


def is_prime(n):
    """Checks if an int is prime

    Args:
        n (int): The number to check

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    """Finds the next highest prime number

    Args:
        n (int): any positive integer.

    Needs: import Math
    """
    if n<2:
        return(2)
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
    """Creates a list of unique prime factors of n

    Args:
        n (int): any positive integer
    """
    check_prime = 2
    prime_factors = [1]
    while check_prime <= math.ceil(n/2):
        if n % check_prime == 0:
            prime_factors.append(check_prime)

            product = 1 #short cut for some numbers
            for num in prime_factors:
                product = product*num
            if product == n:
                return prime_factors

        check_prime = next_prime(check_prime)
    return(prime_factors)

def list_of_prime_factors_mulitplicity(n):
    """Creates a list of prime factors of n and the factor appears accorind to the multiplicity of that nummber

    Args:
        n (int): any positive integer
    """
    check_prime = 2
    prime_factors = [1]
    remainder = n 
    while remainder > 1:
        while remainder % check_prime == 0:
            remainder = remainder / check_prime
            prime_factors.append(check_prime)
        check_prime = next_prime(check_prime)
    return(prime_factors)
