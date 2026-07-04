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