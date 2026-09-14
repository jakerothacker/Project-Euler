# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math

class CompositeNumbers():
    def __init__(self):
        self.num = 9
        self.primes_list = [2,3,5,7]
        self.primes_set = set(self.primes_list)

    def main(self):
        while True:
            if is_prime(self.num):
                self.primes_list.append(self.num)
                self.num+=2
            else:
                Truth = self.check_conject()
                if not Truth:
                    return self.num
                else:
                    self.num +=2
                


    def check_conject(self):
        x=1
        while x**2 < self.num//2:
            for i in reversed(self.primes_list):
                if i + 2*(x**2) == self.num:
                    return(True)
                elif i + 2*(x**2) <self.num:
                    x+=1 
                    break

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




test = CompositeNumbers()
print(test.main())