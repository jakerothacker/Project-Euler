# Find the value of d<1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import math

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


def longest_repeating_decimal(d):
    n = 1
    d_dict = {}

    while n<d:
        n_copy = n
        prime_factors = list_of_prime_factors_mulitplicity(n)
        repeat = False
        for num in prime_factors:
            if num == 1:
                pass
            elif num == 2:
                n_copy = n_copy/2
            elif num == 5:
                n_copy = n_copy/5
            else:
                repeat = True
        if repeat == True:
            ex = 1
            n_copy = int(n_copy)
            while True:
                if (10**ex -1) % n_copy ==0:
                    d_dict[n] = ex
                    break
                ex += 1
        n += 1

    # return max(d_dict , key=d_dict.get)
    return max(d_dict.values())
           

if __name__ == "__main__":
    print (longest_repeating_decimal(1000))





