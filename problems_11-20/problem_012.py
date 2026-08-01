#first triangular number to have over 500 divisors
import math

def next_triangular_number(n):
    """This function gives the next triangular number higher than n

    Args:
        n (float): any number
    Returns:
        int: the next triangular number
    """
    if n < 1:
        return 1
    test = 0
    count = 1
    while test <= n:
        test += count
        count += 1
    return (test)

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

def lowest_triangular_number_divisors(n):
    if n < 1 or n % 1 != 0:
        return print ("Invalid Input")
    tri_num = 1
    tri_count = 1
    while True:
        prime_list = list_of_prime_factors_mulitplicity(tri_num)
        prime_list.pop(0)
        prime_set = set(prime_list)
        count_list = []
        for num in prime_set:
            count_list.append(prime_list.count(num)+1)
        total = 1
        for num in count_list:
            total *= num
        if total >= n:
            return tri_num
        else:
            tri_count += 1
            tri_num += tri_count
        
            

print (lowest_triangular_number_divisors(500))