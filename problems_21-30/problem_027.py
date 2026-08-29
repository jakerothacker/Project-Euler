#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0 .
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

def main():
    a=0
    b=0
    max_a = 0
    max_b = 0
    max_value = 0
    while a<1000:
        b=0
        while b<1000:
            test_1 = find_count(a,b)
            test_2 = find_count(-a,b)
            test_3 = find_count(a,-b)
            test_4 = find_count(-a,-b)
            max_value = max(max_value,test_1,test_2,test_3,test_4)
            if max(max_value,test_1,test_2,test_3,test_4) == test_1:
                max_a = a
                max_b = b
            elif max(max_value,test_1,test_2,test_3,test_4) == test_2:
                max_a = -a
                max_b = b
            elif max(max_value,test_1,test_2,test_3,test_4) == test_3:
                max_a = a
                max_b = -b
            elif max(max_value,test_1,test_2,test_3,test_4) == test_4:
                max_a = -a
                max_b = -b
            b+=1
        a+=1
    return(max_value,max_a,max_b)

def find_count(a,b):
    n = 0
    while True:
        if is_prime(n**2+n*a+b) :
            n+=1
        else:
            return n


if __name__ == "__main__":
    print(main())