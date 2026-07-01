#largest prime factor of 600851475143
import math

def next_prime(n):
    """Finds the next highest prime number

    Args:
        n (int): number that your need the closest higher prime of.
    """
    possible_prime = n + 1
    while True:
        for i in range (2,math.ceil(possible_prime**0.5)):
            if possible_prime % i == 0:
                possible_prime += 1 
                break
            elif i==math.ceil(possible_prime**0.5)-1:
                return(possible_prime)


