# largest palindrome that is the product of two 3-digit numbers
import math



def is_palindrome(n):
    """
    This function checks if a given number is a palindrome.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]
             

def largest_palindrome_product_2_factor(n):
    """
    This gives the largest palindrome that is the product of two n digit numbers
    """
    guess = 10**(2*n) -1
    while len(str(guess))>n:
        if is_palindrome(guess):
            factor_1 = 10**n -1
            while factor_1 >= 10**(n-1):
                factor_2 = guess / factor_1
                if  factor_2 % 1 == 0 and len(str(int(factor_2))) == n:
                    return guess
                    
                else:
                    factor_1 -= 1

        
        guess -= 1
  

print(largest_palindrome_product_2_factor(4))